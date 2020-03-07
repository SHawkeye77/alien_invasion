#This will include functions that make the game work

import sys #Lets us exit the game when the player quits
import pygame #Using pygame for games
from bullet_sideways import BulletSideways #Lets us work with the Bullet class

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #Responding to key being pressed

    if event.key == pygame.K_UP: #Up arrow key
        ship.moving_up = True #Flag for ship moving right is True
    elif event.key == pygame.K_DOWN: #Left arrow key
        ship.moving_down = True #Flag for ship moving left is True
    elif event.key == pygame.K_SPACE: #Space bar
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    #Fires a bullet and keeps track of it (if limit not ret reached)
    if len(bullets) < ai_settings.bullets_allowed: #If there's less bullets than the amount we are allowed in settings, fire bullet
        new_bullet = BulletSideways(ai_settings,screen,ship) #Creating a new bullet
        bullets.add(new_bullet) #Adding the new bullet to the bullets list thing

def check_keyup_events(event,ship):
    #Responding to key being released
    if event.key == pygame.K_UP: #up arrow key
        ship.moving_up = False #Flag for ship moving up is False
    elif event.key == pygame.K_DOWN: #down arrow key
        ship.moving_down = False #Flag for ship moving down is False


def check_events(ai_settings,screen,ship,bullets):
    """Responds to key presses and mouse events"""
    for event in pygame.event.get(): #Runs whenever an event happens
        if event.type == pygame.QUIT: #If game window close button is hit
            sys.exit()
        elif event.type == pygame.KEYDOWN: #If key is pressed
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP: #If key is released
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    """Updates images on the screen and 'flips' (redraws) the screen"""
    
    #Redraw the screen
    screen.fill(ai_settings.bg_color) #The background color depends on what's defined in ai_settings's settings now
    #Redraw the bullets (behind ship and aliens)
    for bullet in bullets.sprites(): #Drawing each bullet
        bullet.draw_bullet()
    ship.blitme() #Update ship
    
    #Make the most recently drawn screen visible:
    pygame.display.flip()

def update_bullets(ship,bullets):
    """Updates position of bullets and gets rid of old bullets"""
    #Updating bullet position
    bullets.update() #updating the entire group of bullets

    #Getting rid of bullets that have left the top of the screen
    for bullet in bullets.copy(): #We use a copy of the group here
        if bullet.rect.left >= ship.screen_rect.right: #Checking if bullet has appeared off top of screen, and if it has remove it from the ACTUAL bullets list (not the copy)
            bullets.remove(bullet)



