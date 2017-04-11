from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify, make_response
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application_db_setup import Base, Console, Game
import random
import string
import re
import httplib2
import json

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = '18d8791553bfba926569'
CLIENT_SECRET = '2b6e9aeed620e62ba1d16248b3ee3c3129d0c17d'


# Helper function to show HTTP errors
def httpResponse(msg, error_code):
    response = make_response(json.dumps(msg), error_code)
    response.headers['Content-Type'] = 'application/json'
    return response


# Show the login page
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', CLIENT_ID=CLIENT_ID, STATE=state)


@app.route('/ghconnect', methods=['POST'])
def gitHubConnect():
    # Check state token sent from the server vs state token from client
    if request.args.get('state') != login_session['state']:
        return httpResponse('Invalid state parameter', 401)

    code = request.get_data()

    # Trade one time code for GitHub API access token
    url = ('https://github.com/login/oauth/access_token?'
           'client_id=%s&client_secret=%s&code=%s'
           % (CLIENT_ID, CLIENT_SECRET, code))
    h = httplib2.Http()
    result = h.request(url, 'POST')[1]
    access_token = re.search('access_token=(.*)&scope', result).group(1)
    print access_token

    # Use access token to retrieve data from the GitHub User API
    if access_token:
        url = ('https://api.github.com/user?access_token=%s' % (access_token))
        h = httplib2.Http()
        user_data = json.loads(h.request(url, 'GET')[1])
        login_session['access_token'] = access_token
    else:
        return httpResponse('Failed to receive access token', 401)

    '''If user data was recieved, add it to the login session for use
    throughout web app'''
    if user_data:
        login_session['github_id'] = user_data['id']
        login_session['name'] = user_data['name']
        login_session['avatar'] = user_data['avatar_url']
        login_session['email'] = user_data['email']
        login_session['username'] = user_data['login']
    else:
        return httpResponse('Faild to retrieve User info', 401)

    # Show users name in the flash message area
    flash('Welcome %s' % login_session['name'].split(' ')[0])
    return 'success'


@app.route('/disconnect')
def gitHubDisconnect():

    # Check if there is a user logged in to disconnect
    if 'name' not in login_session:
        return httpResponse('Current user not connected', 401)

    # Tell GitHub to revoke the current access token
    access_token = login_session['access_token']
    url = ('https://api.github.com/applications/'
           '18d8791553bfba926569/tokens/%s' % access_token)
    h = httplib2.Http()
    headers = ({'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic MThkODc5MTU1M2JmYmE5MjY1Njk6MmI2ZTlhZW'
                'VkNjIwZTYyYmExZDE2MjQ4YjNlZTNjMzEyOWQwYzE3ZA=='})
    result = h.request(url, 'DELETE', headers=headers)

    # Log user out of the application
    if result[0]['status'] == '204':

        del login_session['name']
        del login_session['avatar']
        del login_session['email']
        del login_session['access_token']
        del login_session['state']

        flash('You have been successfully logged out')
        return redirect('/')
    else:
        return httpResponse('Failed to revoke token for given user.', 400)


@app.route('/')
def showConsoles():
    # Generate state token.
    state = (''.join(random.choice(string.ascii_uppercase + string.digits)
             for x in xrange(32)))
    login_session['state'] = state

    consoles = session.query(Console).all()
    # Create an array of the most recent game for each console.
    recent_games = []
    for console in consoles:
        recent_games.append(session.query(Game).filter_by(
                            console_id=console.id).order_by(
                            Game.id.desc()).all()[0])

    return render_template('allConsoles.html', consoles=consoles,
                           recent_games=recent_games, CLIENT_ID=CLIENT_ID,
                           STATE=state)


@app.route('/console/<int:console_id>')
def showGamesByConsole(console_id):
    consoles = session.query(Console).all()
    console = session.query(Console).filter_by(id=console_id).one()
    games = session.query(Game).filter_by(console_id=console_id).all()
    return render_template('gamesByConsole.html',
                           consoles=consoles, console=console, games=games)


@app.route('/console/<int:console_id>/game/<int:game_id>')
def showGame(console_id, game_id):
    game = (session.query(Game).filter_by(
            console_id=console_id, id=game_id).one())
    return render_template('showGame.html', game=game)


@app.route('/console/<int:console_id>/game/<int:game_id>/delete',
           methods=['GET', 'POST'])
def deleteGame(console_id, game_id):
    if 'name' not in login_session:
        flash('Please login to delete game!')
        return redirect('/')
    console = session.query(Console).filter_by(id=console_id).one()
    game = (session.query(Game).filter_by(
            console_id=console_id, id=game_id).one())
    if request.method == 'POST':
        if game:
            session.delete(game)
            session.commit()
            return redirect(url_for(
                            'showGamesByConsole', console_id=console_id))
    else:
        return render_template('deleteGame.html', game=game)


@app.route('/console/<int:console_id>/game/<int:game_id>/edit',
           methods=['GET', 'POST'])
def editGame(console_id, game_id):
    if 'name' not in login_session:
        flash('Please login to edit game!')
        return redirect('/')
    console = session.query(Console).filter_by(id=console_id).one()
    game = (session.query(Game).filter_by(
            console_id=console_id, id=game_id).one())
    if request.method == 'POST':
        if game:
            # Get game details from edit form.
            game.name = request.form['name']
            game.company = request.form['company']
            game.cost = request.form['cost']
            game.description = request.form['description']
            game.picture = request.form['picture']

            # Update the Game object.
            session.add(game)
            session.commit()

            # Show the Game with updated details.
            return redirect(url_for('showGame',
                                    console_id=console_id,
                                    game_id=game_id))
    else:
        return render_template('editGame.html', game=game)


@app.route('/new', methods=['GET', 'POST'])
def newGame():
    if 'name' not in login_session:
        flash('Please login to add new games!')
        return redirect('/')
    consoles = session.query(Console).all()
    if request.method == 'POST':
        # Ensure all fields are filled in.
        if (request.form['name'] and request.form['cost'] and
            request.form['company'] and request.form['description'] and
                request.form['picture']):
            # Create a new Game based on the new game form contents.
            game = Game(name=request.form['name'],
                        cost=request.form['cost'],
                        company=request.form['company'],
                        description=request.form['description'],
                        picture=request.form['picture'],
                        console_id=request.form['console'])
            session.add(game)
            session.commit()
            return redirect(url_for('showGame',
                                    console_id=game.console_id,
                                    game_id=game.id))
        else:
            """ Show error and preserve field contents if all
                 fields are not filled in."""
            flash('Please fill in all fields!')
            return render_template('newGame.html',
                                   consoles=consoles,
                                   fields=request.form)
    else:
        return render_template('newGame.html', consoles=consoles, fields=[])


@app.route('/games.json')
def gamesJSON():
    consoles = session.query(Console).all()
    json_array = []
    for console in consoles:
        games_array = []
        games = session.query(Game).filter_by(console_id=console.id).all()
        for game in games:
            games_array.append({
                'name': game.name,
                'id': game.id,
                'cost': game.cost,
                'description': game.description,
                'company': game.company,
                'picture': game.picture
            })
        json_array.append({'id': console.id,
                           'name': console.name,
                           'games': games_array})
    return jsonify(Games=json_array)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
