from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application_db_setup import Base, Console, Game

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#PC
console1 = Console(name = "PC", picture = "http://www.gamestop.com/common/images/lbox/139343b.jpg")

session.add(console1)
session.commit()

game1 = Game(name="The Sims 4", company="Electronic Arts", picture="http://www.gamestop.com/common/images/lbox/525786b1.jpg", cost=39.99, description="The Sims 4 is the highly anticipated life simulation game that lets you play with life like never before. Control smarter Sims with unique appearances, personalities, behaviors, and emotions. Experience new levels of creativity when you sculpt Sims with the powerful Create A Sim and design beautiful homes with tactile, room-based Build Mode.", console = console1)

session.add(game1)
session.commit()

game2 = Game(name="Guild Wars Trilogy", company="NCSOFT", picture="http://www.gamestop.com/common/images/lbox/647449b.jpg", cost=29.99, description="Step into Guild Wars, the award-winning fantasy online role-playing game enjoyed by millions of players. For the first time ever, Guild Wars Trilogy combines Guild Wars, Factions, and Nightfall into a single amazing experience.", console = console1)

session.add(game2)
session.commit()

game3 = Game(name="The Elder Scrolls V: Skyrim", company="Bethesda Softworks", picture="http://www.gamestop.com/common/images/lbox/521618b2.jpg", cost=19.99, description="The next chapter in the highly anticipated Elder Scrolls saga arrives from the makers of the 2006 and 2008 Games of the Year, Bethesda Game Studios. Skyrim reimagines and revolutionizes the open-world fantasy epic, bringing to life a complete virtual world open for you to explore any way you choose.", console = console1)

session.add(game3)
session.commit()

game4 = Game(name="Grand Theft Auto V", company="Rockstar Games", picture="http://www.gamestop.com/common/images/lbox/102049b.jpg", cost=59.99, description="Grand Theft Auto V for PC offers players the option to explore the award-winning world of Los Santos and Blaine County in resolutions of up to 4k and beyond, as well as the chance to experience the game running at 60 frames per second.", console = console1)

session.add(game4)
session.commit()

# Playstation 4

console2 = Console(name = "Playstation 4", picture = "http://www.gamestop.com/common/images/lbox/131991b.jpg")

session.add(console2)
session.commit()

game1 = Game(name="Injustice 2", company="Warner Home Video Games", picture="http://www.gamestop.com/common/images/lbox/126581brp2.jpg", cost=59.99, description="Power up and build the ultimate version of your favorite DC legends in INJUSTICE 2. With a massive selection of DC Super Heroes and Super-Villains, INJUSTICE 2 allows you to equip every iconic character with unique and powerful gear earned throughout the game.", console = console2)

session.add(game1)
session.commit()

game2 = Game(name="Horizon Zero Dawn", company="Sony Computer Entertainment America", picture="http://www.gamestop.com/common/images/lbox/123788b.jpg", cost=59.99, description="Horizon Zero Dawn is an exhilarating new action role playing game exclusively for the PlayStation4 System, developed by the award-winning Guerrilla Games, creators of PlayStation's venerated Killzone franchise.", console = console2)

session.add(game2)
session.commit()

game3 = Game(name="UNCHARTED 4: A Thief's End", company="Sony Computer Entertainment", picture="http://www.gamestop.com/common/images/lbox/103729b.jpg", cost=39.99, description="Several years after his last adventure, retired fortune hunter, Nathan Drake, is forced back into the world of thieves. With the stakes much more personal, Drake embarks on a globe-trotting journey in pursuit of a historical conspiracy behind a fabled pirate treasure.", console = console2)

session.add(game3)
session.commit()

game4 = Game(name="Lego Worlds", company="Warner Home Video Games", picture="http://www.gamestop.com/common/images/lbox/138635b.jpg", cost=59.99, description="EXPLORE. DISCOVER. CREATE. TOGETHER. LEGO Worlds is an open environment of procedurally-generated Worlds made entirely of LEGO bricks which you can freely manipulate and dynamically populate with LEGO models.", console = console2)

session.add(game4)
session.commit()

# Wii U

console3 = Console(name = "Wii U", picture = "http://www.gamestop.com/common/images/lbox/909260b.jpg")

session.add(console3)
session.commit()

game1 = Game(name="The Legend of Zelda: Breath of the Wild", company="Nintendo", picture="http://www.gamestop.com/common/images/lbox/127484b.jpg", cost=59.99, description="Forget everything you know about The Legend of Zelda games. Step into a world of discovery, exploration and adventure in The Legend of Zelda: Breath of the Wild, a boundary-breaking new game in the acclaimed series.", console = console3)

session.add(game1)
session.commit()

game2 = Game(name="Mario Party 10", company="Nintendo of America", picture="http://www.gamestop.com/common/images/lbox/108006b.jpg", cost=29.99, description="Bowser crashes the latest Mario Party, the first installment of the series on the Wii U console. In the new Bowser Party Mini-games, play as Bowser himself and face off against up to four others playing as Mario and friends.", console = console3)

session.add(game2)
session.commit()

game3 = Game(name="Super Smash Bros.", company="Nintendo of America", picture="http://www.gamestop.com/common/images/lbox/240274b.jpg", cost=59.99, description="Mario! Link! Samus! Pikachu! All of your favorite Nintendo characters are back, along with plenty of new faces, in Super Smash Bros. for Wii U, the next entry in the beloved Super Smash Bros. series. Up to four players can battle each other locally or online across beautifully designed stages inspired by classic Nintendo home console games.", console = console3)

session.add(game3)
session.commit()

game4 = Game(name="Mario Kart 8", company="Nintendo of America", picture="http://www.gamestop.com/common/images/lbox/240262b.jpg", cost=59.99, description="Feel the rush as your kart rockets across the ceiling! Race upside-down and along walls on anti-gravity tracks in the most action-fueled Mario Kart game yet! Take on racers across the globe and share videos of your greatest moments via Mario Kart TV.", console = console3)

session.add(game4)
session.commit()

# Xbox One

console4 = Console(name = "Xbox One", picture = "http://www.gamestop.com/common/images/lbox/101371b.jpg")

session.add(console4)
session.commit()

game1 = Game(name="Destiny 2", company="Activision", picture="http://www.gamestop.com/common/images/lbox/146355brp.jpg", cost=59.99, description="From the makers of the acclaimed hit game Destiny, comes the much-anticipated sequel. An action shooter that takes you on an epic journey across the solar system.", console = console4)

session.add(game1)
session.commit()

game2 = Game(name="Tom Clancy's Ghost Recon Wildlands", company="UbiSoft", picture="http://www.gamestop.com/common/images/lbox/125810b.jpg", cost=59.99, description="Experience total freedom of choice in Tom Clancy's Ghost Recon Wildlands, the ultimate military shooter set in a massive open world setting.", console = console4)

session.add(game2)
session.commit()

game3 = Game(name="Diablo III Ultimate Evil Edition", company="Blizzard Entertainment", picture="http://www.gamestop.com/common/images/lbox/101348b1.jpg", cost=19.99, description="Face Ultimate Evil Over 13 million players have battled the demonic hordes of Diablo III. Now, it's your turn to join the crusade and take up arms against the enemies of the mortal realms. This Ultimate Evil Edition contains both Diablo III and the Reaper of Souls expansion set, together in one definitive volume. So stand ready. Something wicked this way comes.", console = console4)

session.add(game3)
session.commit()

game4 = Game(name="Titanfall", company="Electronic Arts", picture="http://www.gamestop.com/common/images/lbox/210026b.jpg", cost=49.99, description="Prepare for Titanfall. Crafted by one of the co-creators of Call of Duty and other key developers behind the Call of Duty franchise, Titanfall is an all-new universe juxtaposing small vs. giant, natural vs. industrial and man vs. machine.", console = console4)

session.add(game4)
session.commit()

print "Categories and Items successfully added!"
