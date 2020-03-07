import pygame
from settings import Settings #Contains the class with all settings for the game (recycling from alien_invasion settings)
from bucket import Bucket #Gets us info about our bucket
from apple import Apple
import apple_bucket_game_functions as abgf
from game_stats_apple_bucket import GameStats

def run_game():
    """The function that runs the game"""

    #Initialize pygame and settings
    pygame.init()
    ai_settings = Settings() #creating 'ai_settings' from our imported Settings class, which acts as the overall settings for our game

    #Initializing 'screen' surface
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #Initializing screen size
    pygame.display.set_caption("Apple Bucket Game") #Captioning our screen (the window we play in)
    bg_color = (ai_settings.bg_color) #Setting background color

    #Making a bucket and apple:
    bucket = Bucket(ai_settings,screen)
    apple = Apple(ai_settings,screen)

    #Creating an instance that represents our stats
    stats = GameStats(ai_settings)

    #Starting the main loop for the game:
    while True:

        abgf.check_events(ai_settings,screen,bucket) #Checking for events (player input)
        
        #If still have lives
        if stats.game_active:
            bucket.update() #Updates bucket position
            apple = abgf.update_apple(ai_settings,apple,screen,bucket,stats) #Updating falling apple or redraws if it collided or hit bottom
            apple.blitme()
        
        abgf.update_screen(ai_settings,screen,bucket,apple) #Drawing updates things on the screen







run_game()

    
