import pygame #Contains the functions used to create a game
from settings import Settings #Contains the class with all our settings for the game
from ship import Ship #Contains the class to create a ship
import game_functions as gf #Imports the game_functions module nicknamed gf
from pygame.sprite import Group #Imports the Group class (behaves like a list but with extra functionality)
from game_stats import GameStats #Imports the stats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """The function that runs the game"""

    #Initialize pygame and settings
    pygame.init()
    ai_settings = Settings() #creating 'ai_settings' from our imported Settings class, which acts as the overall settings for our game

    #Initializing 'screen' surface
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #Initializing screen size
    pygame.display.set_caption("Alien Invasion") #Captioning our screen (the window we play in)
    bg_color = (ai_settings.bg_color) #Setting background color
    
    #Creating the play button
    play_button = Button(ai_settings,screen,"Play")

    #Creating an instance to store stats and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #Making a ship, group of bullets, and a group of aliens
    ship = Ship(ai_settings,screen) #Making a ship from our ship class
    bullets = Group()
    aliens = Group()
    
    #Create the actual fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #Loading the background music for the game and playing it
    pygame.mixer.music.load('space_loop.wav')
    pygame.mixer.music.play(-1) #Playing the background music constantly till I tell it to stop

    #Starting the main loop for the game:
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets) #Checking for events (player input)
        
        #If you still have ships left the following runs...
        if stats.game_active:  
            ship.update() #Updates ship position
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets) #Updating bullets
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets) #Updating aliens
        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) #Drawing updates things on the screen


run_game()

# To run this game in python 2.7.9 (since I wrote it in that and have since updated to 3.7),
# go to terminal and...
#1. navigate to the file: 
#       >>> cd desktop/python_work/alien_invasion
#2. run the "run_game" function using python 2 
#       >>> python2 -c 'import alien_invasion; alien_invasion.run_game()'




