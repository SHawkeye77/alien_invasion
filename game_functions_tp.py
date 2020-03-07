import sys #Lets us exit the game when the player quits
import pygame #Using pygame for games
from alien import Alien #Gives access to the Alien class which creates individual aliens
from bullet_tp import Bullet #Lets us work with the Bullet class
from target_tp import Target

def check_events(ai_settings,screen,stats,play_button,ship,bullets):
    """Responds to key presses and mouse events"""
    for event in pygame.event.get(): #Runs whenever an event happens
        if event.type == pygame.QUIT: #If game window close button is hit
            sys.exit()
        elif event.type == pygame.KEYDOWN: #If key is pressed
            check_keydown_events(event,ai_settings,screen,ship,bullets,stats)
        elif event.type == pygame.KEYUP: #If key is released
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN: #Checks if mouse hits something
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,bullets,mouse_x,mouse_y)

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats):
    #Responding to key being pressed

    if event.key == pygame.K_UP: #Up arrow key
        ship.moving_up = True #Flag for ship moving right is True
    elif event.key == pygame.K_DOWN: #Down arrow key
        ship.moving_down = True #Flag for ship moving left is True
    elif event.key == pygame.K_SPACE: #Space bar
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q: #'q' key
        sys.exit() #Adds a shortcut to exit the game

def check_keyup_events(event,ship):
    #Responding to key being released
    if event.key == pygame.K_UP: #Up arrow key
        ship.moving_up = False #Flag for ship moving up is False
    elif event.key == pygame.K_DOWN: #Down arrow key
        ship.moving_down = False #Flag for ship moving down is False

def check_play_button(ai_settings,screen,stats,play_button,ship,bullets,mouse_x,mouse_y):
    #Starts a new game when the player clicks play OR presses the 'p' button
    
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    
    #If the play button has been clicked and the game is NOT active...
    if button_clicked and not stats.game_active:
        
        #Reset the dynamic settings
        ai_settings.initialize_dynamic_settings()

        #Hide mouse cursor
        pygame.mouse.set_visible(False)



        #Reset the game stats.
        stats.reset_stats()
        stats.game_active = True

        #Empty the list of bullets
        bullets.empty()

        #Create a new target and centers the ship
        create_target(ai_settings,screen)
        ship.center_ship()

def fire_bullet(ai_settings,screen,ship,bullets):
    #Fires a bullet and keeps track of it (if limit not ret reached)
    if len(bullets) < ai_settings.bullets_allowed: #If there's less bullets than the amount we are allowed in settings, fire bullet
        new_bullet = Bullet(ai_settings,screen,ship) #Creating a new bullet
        bullets.add(new_bullet) #Adding the new bullet to the bullets list thing


def create_target(ai_settings,screen):
    #Creates and draws a new target
    target = Target(ai_settings,screen)
    target.draw_target()

def update_bullets(ai_settings,screen,ship,target,bullets,stats,misses):
    """Updates position of bullets, gets rid of old bullets, gets rid of hit aliens, replenishes fleet."""
        
    #Creating a rect to work with the screen with 
    screen_rect = screen.get_rect()
    
    #Updating bullet position
    bullets.update() #updating the entire group of bullets

    #Getting rid of bullets that have left the right of the screen
    #Checking if bullet collides with target. If so, remove it.
    for bullet in bullets.copy(): #We use a copy of the group here
        if bullet.rect.left >= screen_rect.right: #Checking if bullet has appeared off right of screen, and if it has remove it from the ACTUAL bullets list (not the copy)
            bullets.remove(bullet)
            
            #If this is more than alloted misses, end the game. Otherwise, just add a miss to the counter
            if stats.misses_left > 0:
                stats.misses_left -= 1
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)

        elif pygame.sprite.collide_rect(target,bullet):
            bullets.remove(bullet)
            ai_settings.increase_speed()

def update_target(ai_settings,target,screen):
    #Moving target up and down
    screen_rect = screen.get_rect()
    
    #Switching directions if the target hits an edge
    if target.rect.bottom >= screen_rect.bottom:
        ai_settings.target_direction *= -1 
    elif target.rect.top <= 0:
        ai_settings.target_direction *= -1 

    #Moving the target up or down
    target.rect.centery += (ai_settings.target_speed * ai_settings.target_direction)

def update_screen(ai_settings,screen,stats,target,ship,bullets,play_button):
    """Updates images on the screen and 'flips' (redraws) the screen"""

    #Redraw the screen
    screen.fill(ai_settings.bg_color) #The background color depends on what's defined in ai_settings's settings now
    
    #If the game is inactive, draw the play button
    if not stats.game_active: #If game is not active...
        play_button.draw_button()

        #Show mouse cursor
        pygame.mouse.set_visible(True)

        #Reset the game stats.
        stats.reset_stats()

        #Empty the list of bullets
        bullets.empty()

        #Create a new target and centers the ship
        create_target(ai_settings,screen)
        ship.center_ship()

    #Redraw the target
    target.draw_target()
    
    #Redraws the ship
    ship.blitme()
    
    #Redraw the bullets (behind ship)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    #Make the most recently drawn screen visible:
    pygame.display.flip()





