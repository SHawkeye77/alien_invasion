import sys #Lets us exit the game when the player quits
import pygame #Using pygame for games
from apple import Apple #Gives access to the Apple class which creates apples
from game_stats_apple_bucket import GameStats #Import game stats

def check_events(ai_settings,screen,bucket):
    """Responds to key presses and mouse events"""
    for event in pygame.event.get(): #Runs whenever an event happens
        if event.type == pygame.QUIT: #If game window close button is hit
            sys.exit()
        elif event.type == pygame.KEYDOWN: #If key is pressed
            check_keydown_events(event,ai_settings,screen,bucket)
        elif event.type == pygame.KEYUP: #If key is released
            check_keyup_events(event,bucket)

def check_keyup_events(event,bucket):
    #Responding to key being released
    if event.key == pygame.K_RIGHT: #Right arrow key
        bucket.moving_right = False #Flag for bucket moving right is False
    elif event.key == pygame.K_LEFT: #Left arrow key
        bucket.moving_left = False #Flag for bucket moving left is False

def check_keydown_events(event,ai_settings,screen,bucket):
    #Responding to key being pressed

    if event.key == pygame.K_RIGHT: #Right arrow key
        bucket.moving_right = True #Flag for bucket moving right is True
    elif event.key == pygame.K_LEFT: #Left arrow key
        bucket.moving_left = True #Flag for bucket moving left is True
    elif event.key == pygame.K_q: #'q' key
        sys.exit() #Adds a shortcut to exit the game           

def update_apple(ai_settings,apple,screen,bucket,stats):
    """Having the apple fall continuously on screen until a collision"""
    """If it collides with bucket, then redraw at the top"""
    screen_rect = screen.get_rect()
    
    if stats.lives_left > 0 : #If the player still has remaining lives...
        if pygame.Rect.colliderect(apple.rect,bucket.rect): #If a collision was detected anywhere on the apple and bucket rectangles...
            apple = Apple(ai_settings,screen) #...create a new apple at the top of the screen
        elif apple.rect.bottom > screen_rect.bottom: #If the apple has hit bottom of screen...
            stats.lives_left -= 1
            apple = Apple(ai_settings,screen) #...create a new apple at the top of the screen
        else: #If no collision nor does it hit bot of screen, update its pos and say apple is same apple
            apple.rect.y += ai_settings.alien_speed_factor #For simplicity - making the apple fall same as alien falls
            apple = apple
    else:
        stats.game_active = False

    return apple #Return apple no matter what

def update_screen(ai_settings,screen,bucket,apple):
    """Updates images on the screen and 'flips' (redraws) the screen"""
    
    #Redraw the screen
    screen.fill(ai_settings.bg_color) #The background color depends on what's defined in ai_settings's settings now
    
    #Redraws the bucket
    bucket.blitme()

    #Redraw the alien fleet
    apple.blitme()
    
    #Make the most recently drawn screen visible:
    pygame.display.flip()


