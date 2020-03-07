#We need to do the following:
#1. Create a ship in the left center of the screen
#2. Let the player move the ship up and down
#3. Let the ship shoot bullets that are deleted once they leave the screen.

import pygame #Contains the functions used to create a game
from settings import Settings #Contains the class with all our settings for the game
from ship_sideways import ShipSideways #Contains the class to create a ship
import game_functions_sideways as gf #Imports the game_functions_sideways module nicknamed gf
from pygame.sprite import Group #Imports the Group class (behaves like a list but with extra functionality)

def run_game():
    """The function that runs the game"""

    #Initialize pygame and settings
    pygame.init()
    ai_settings = Settings() #creating 'ai_settings' from our imported Settings class, which acts as the overall settings for our game

    #Initializing 'screen' surface
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #Initializing screen size
    pygame.display.set_caption("Alien Invasion Sideways") #Captioning our screen (the window we play in)
    bg_color = (ai_settings.bg_color) #Setting background color
    
    #Initializing 'ship' surface
    ship = ShipSideways(ai_settings,screen) #Making a ship from our ship class

    #Initializing the group of bullets in the "Group" class
    bullets = Group()


    #Starting the main loop for the game:
    while True:
        gf.check_events(ai_settings,screen,ship,bullets) #Checking for events (player input)
        ship.update() #Updates ship position
        gf.update_bullets(ship,bullets) #Updating bullets
        gf.update_screen(ai_settings,screen,ship,bullets) #Drawing updates things on the screen

        











run_game()