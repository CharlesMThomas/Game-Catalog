# Game Catalog

By: Charles M Thomas

**Game Catalog** is Python program that uses a Sqlite database to keep track of best selling video games across a range of gaming devices. The most recently added game for each device is shown on the home screen. Clicking on a specific gaming device, shows all best selling games for that device. Logged in users are able to add, edit and delete games from Game Catalog. Users are able to login via their GitHub account. Guests may only browse the site and cannot make any changes.

Game Catalog was built and tested using Linux via VirtualBox. VirtualBox was configured using Vagrant. If you are already running Ubuntu and would like to run Tournament Results locally (not in VirtualBox), please skip to the *Installing Dependencies* section below.

## Installing VirtualBox

* Download the installtion file for your operating system here: https://www.virtualbox.org/wiki/Downloads
* Run the installation file and follow the instructions.
* You do not need the extension pack or the SDK. 
* You do not need to launch VirtualBox after installing it; Vagrant will do that.

## Installing Vagrant

* Download the installation file for your operating system here: https://www.vagrantup.com/downloads.html
* Run the installation file and follow the instructions.
* Windows Users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Preparing to run the VirtualBox Ubuntu Installation

* Download the VirtualBox configuration files from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488015_fsnd-virtual-machine/fsnd-virtual-machine.zip
* Extract the FSND-Virtual-Machine folder from the zip file.
* Navigate to the FSND-Virtual-Machine folder via terminal or GitBash
  * Windows Users: Download the Unix-style terminal GitBash from here: https://git-scm.com/downloads
* Change directories to **vagrant**

## Starting the VirtualBox Ubuntu Installation

Use the vagrant up command to start the Ubuntu Linux installation within VirtualBox

`vagrant up`

Log into the VirtualBox Ubuntu installation that was created in the previous step

`vagrant ssh`

If you were successfully logged in, you should see the following shell prompt:

`vagrant@vagrant-ubuntu-trusty-32:~$`

## Installing Dependencies

**The VirtualBox Ubuntu installation from the steps above has been preconfigured with all of the required dependencies for running Tournament Results.**

If you are running Ubuntu locally, the following dependencies are required:

**Flask - Micro webdevelopment framework for Python**

`sudo pip install flask`

**SQLAlchemy - A Python SQL toolkit and Object Relational Mapper**

`sudo pip install sqlalchemy`

**httplib2 - Python HTTP request/response library**

`sudo pip install httplib2`

## Setting up the Sqlite database

#### Local Machine (not the VirtualBox) or Local Linux: 

Download the files from this repository and place them within the **FSND-Virtual-Machine\vagrant** folder.

#### VirtualBox or Local Linux: 

Navigate to the game catalog directory

`cd vagrant\game-catalog`

Run the Sqlite SQL file for database and table creation

`python application_db_setup.py`

Run the database seed file to load the dummy data

`python lotsofgames.py`

## Starting the Game Catalog App

Run the application

`python application.py`

Open the application in your web browser

*Web Address: http://localhost:5000/*

## Using the Game Catalog App

#### Browsing Games (Guest or Logged In )

* Click any of the best selling games on the home page.
* Click a specific gaming device, to see games for only that device.

#### Logging In

* Click the login button at the top of the site.
* Click the 'Login with GitHub' button on the login page.
* Enter your GitHub login credentials and authorize the Game Catalog App.
* If login was successful, you will be redirected back to the home page showing a logged in status.

#### Adding a Game (Must be Logged In)

* Click the 'Add Game' button at the top of the site.
* Fill out all fields on the new game page.
* Click the 'Submit' button.
* If the game was successfully added, you will be redirected to the new games details page.

#### Editing a Game (Must be Logged In)

* Click on a game from either the home page or device page to view game detail page.
* Click the 'Edit' button below the game description.
* Change the contents of any of the game details fields.
* Click the 'Submit' button.
* If the game was successfully updated, you will be redirected back to the game's detail page.

#### Deleting a Game (Must be Logged In)

* Click on a game from either the home page or device page to view game detail page.
* Click the 'Yes' button when asked if you really want to delete the game on the game delete page.
* If the game was successfully deleted, you will be redirected back to the games for that gaming device.

#### Logging Out (Must be Logged In)

* Click the logout button at the top of the screen.
* If logout was successful, you will see a logged out message at the top of the screen.

## Accessing JSON endpoint

* All data from Game Catalog can be access the following JSON endpoint:

*Web Address: http://localhost:5000/games.json*