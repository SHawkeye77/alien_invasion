import pygame #Contains the functions used to create a game
from settings_tp import Settings #Contains the class with all our settings for the game
from game_stats_tp import GameStats #Imports the stats
from ship_tp import Ship
import game_functions_tp as gf
from target_tp import Target
from button_tp import Button
from pygame.sprite import Group #Imports the Group class (behaves like a list but with extra functionality)

def run_game():
    """The function that runs the game"""

    #Initialize pygame and settings
    pygame.init()
    ai_settings = Settings() #creating 'ai_settings' from our imported Settings class, which acts as the overall settings for our game

    #Initializing 'screen' surface
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #Initializing screen size
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Target Practice") #Captioning our screen (the window we play in)
    bg_color = (ai_settings.bg_color) #Setting background color
    
    #Creating the play button
    play_button = Button(ai_settings,screen,"Play Game")

    #Creating an instance that will hold all our game statistics
    stats = GameStats(ai_settings)

    #Making a ship, group of bullets, and a target
    ship = Ship(ai_settings,screen) #Making a ship from our ship class
    bullets = Group()
    target = Target(ai_settings,screen)

    #Starting the main loop for the game:
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,bullets) #Checking for events (player input)
        
        #If you still have shots left the following runs...
        if stats.game_active:    
            ship.update() #Updates ship position
            gf.update_bullets(ai_settings, screen, ship, target, bullets, stats, stats.misses_left) #Updating bullets and removing bullets if necessary. Makes game over if alloted bullets were missed.
            gf.update_target(ai_settings,target,screen) #Moves target up and down, switching directions when it hits walls
        gf.update_screen(ai_settings,screen,stats,target,ship,bullets,play_button) #Drawing updates things on the screen









run_game()