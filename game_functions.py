#This will include functions that make the game work

import sys #Lets us exit the game when the player quits
import pygame #Using pygame for games
from alien import Alien #Gives access to the Alien class which creates individual aliens
from bullet import Bullet #Lets us work with the Bullet class
from time import sleep #Allows for "pauses"
import json

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """Responds to key presses and mouse events"""
    for event in pygame.event.get(): #Runs whenever an event happens
        if event.type == pygame.QUIT: #If game window close button is hit
            check_for_global_high_score(stats)
            sys.exit()        
        elif event.type == pygame.KEYDOWN: #If key is pressed
            check_keydown_events(event,ai_settings,screen,ship,bullets,stats)
        elif event.type == pygame.KEYUP: #If key is released
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN: #Checks if mouse hits something
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats):
    #Responding to key being pressed

    if event.key == pygame.K_RIGHT: #Right arrow key
        ship.moving_right = True #Flag for ship moving right is True
    elif event.key == pygame.K_LEFT: #Left arrow key
        ship.moving_left = True #Flag for ship moving left is True
    elif event.key == pygame.K_SPACE: #Space bar
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q: #'q' key
        check_for_global_high_score(stats)
        sys.exit() #Adds a shortcut to exit the game

def check_for_global_high_score(stats):
    """If local high score is larger than current high score, replace it"""
    with open('global_high.json') as f_obj:
        global_high = json.load(f_obj)
        if stats.high_score > global_high:
            with open('global_high.json','w') as f_obj_2:
                json.dump(stats.high_score,f_obj_2)

def check_keyup_events(event,ship):
    #Responding to key being released
    if event.key == pygame.K_RIGHT: #Right arrow key
        ship.moving_right = False #Flag for ship moving right is False
    elif event.key == pygame.K_LEFT: #Left arrow key
        ship.moving_left = False #Flag for ship moving left is False

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #Starts a new game when the player clicks play OR presses the 'p' button
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    
    #If the play button has been clicked and the game is NOT active...
    if button_clicked and not stats.game_active:
        #Hide mouse cursor
        pygame.mouse.set_visible(False)

        #Reset the game stats.
        stats.reset_stats()
        stats.game_active = True

        #Empty the list of bullets and aliens
        bullets.empty()
        aliens.empty()

        #Reset the scoreboard images
        sb.prep_images()

        #Start up the background music again
        pygame.mixer.music.play(-1) #Playing the background music constantly till I tell it to stop

        #Resetting the dynamic settings
        ai_settings.initialize_dynamic_settings()

        #Create a new fleet and center the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


def fire_bullet(ai_settings,screen,ship,bullets):
    #Fires a bullet and keeps track of it (if limit not ret reached)
    bullet_sound = pygame.mixer.Sound('laser_shot.wav')
    if len(bullets) < ai_settings.bullets_allowed: #If there's less bullets than the amount we are allowed in settings, fire bullet
        bullet_sound.play()
        new_bullet = Bullet(ai_settings,screen,ship) #Creating a new bullet
        bullets.add(new_bullet) #Adding the new bullet to the bullets list thing

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Updates position of bullets, gets rid of old bullets, gets rid of hit aliens, replenishes fleet."""
    
    #Updating bullet position
    bullets.update() #updating the entire group of bullets

    #Getting rid of bullets that have left the top of the screen
    for bullet in bullets.copy(): #We use a copy of the group here
        if bullet.rect.bottom <= 0: #Checking if bullet has appeared off top of screen, and if it has remove it from the ACTUAL bullets list (not the copy)
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets) #Checks for collisions and replenishes destroyed fleet.

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """Updates images on the screen and 'flips' (redraws) the screen"""
    
    #Redraw the screen
    screen.fill(ai_settings.bg_color) #The background color depends on what's defined in ai_settings's settings now
    
    #Draw the score information.
    sb.show_score()

    #Redraw the bullets (behind ship and aliens)
    for bullet in bullets.sprites(): #Drawing each bullet
        bullet.draw_bullet()

    #Redraws the ship
    ship.blitme()

    #Redraw the alien fleet
    aliens.draw(screen)
    
    #If the game is inactive, draw the play button
    if not stats.game_active: #If game is not active...
        play_button.draw_button()

    #Make the most recently drawn screen visible:
    pygame.display.flip()

  
def check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Checks for collision b/w bullets and aliens and destroys them if they collide. Also replaces a fleet with a speedier one if fully destroyed"""
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True) #'collisions' is a dictionary that has key:value pairs that are the bullet then the alien that were hit
    explosion_sound = pygame.mixer.Sound('explosion.wav')
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        explosion_sound.play() #Play explosion sound
        check_high_score(stats,sb)
    if len(aliens) == 0: #If theres no aliens left, we get rid of all remaining bullet sprites then create a new fleet
        start_new_level(bullets,ai_settings,stats,sb,screen,ship,aliens)

def start_new_level(bullets,ai_settings,stats,sb,screen,ship,aliens):
    """Starts new level"""
    
    #Play new level sound
    new_level_sound = pygame.mixer.Sound('level_up.wav')
    new_level_sound.play()

    #If entire fleet is destroyed, start a new level
    bullets.empty() #Empties the group
    ai_settings.increase_speed()
    create_fleet(ai_settings,screen,ship,aliens)

    #increase level.
    stats.level += 1
    sb.prep_level()

def get_number_aliens_x(ai_settings,alien_width):
    """Determines the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - (2 * alien_width) #Available space horizontally to make aliens (leaving blank space of alien on either end)
    number_aliens_x = int(available_space_x / (2 * alien_width)) #Calculates (closest integer) number of aliens in one row if we leave a space of one alien width between each
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """Returns the number of rows of aliens that fit the screen"""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height #Available space is the space 3 alien lengths above the ship
    number_rows = int(available_space_y / (2 * alien_height)) #calculating (integer) number of rows assuming one alien height of space is left open between each
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """Creates an alien and places it"""
    alien = Alien(ai_settings,screen) #Creating an alien to add to the fleet
    alien_width = alien.rect.width #Making a width attribute to use (from the alien we just created)
    alien.x = (alien_width + 2 * alien_number * alien_width) #Defining a value the x position of each alien...
    alien.rect.x = alien.x #...and then actually putting the value into action by assigning it to the rect attribute.
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number) #Defining y-value of rect leaving a space for an alien in between each
    aliens.add(alien) #Adding the alien to the fleet list

def create_fleet(ai_settings,screen,ship,aliens):
    """Creates a full fleet of aliens"""
    alien = Alien(ai_settings,screen) #Creating a single alien. This will NOT be added to the fleet. It is only used to use its dimensions
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width) #Calls the get_number_aliens_x function to see how many aliens can fit on screen. 
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height) #Determining number of rows of aliens we can have

    #Creating fleet of aliens:
    for row_number in range(number_rows): #Making the following row the amount of times calculated by number_rows
        for alien_number in range(number_aliens_x): #Will be done equal to the amount of times suggested by number_aliens_x
            #Create an alien and place it in the row.
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    """Respond appropriately if any aliens have reached the edge."""
    for alien in aliens.sprites(): #Calls each alien in the "sprites list", aliens
        if alien.check_edges(): #If this returns true, an alien has hit the side of the screen, so we gotta...
            change_fleet_direction(ai_settings,aliens) #...drop and change direction
            break #Once this is detected one time, we know to change direction.

def change_fleet_direction(ai_settings,aliens):
    """Drop the entire fleet and change direction"""
    for alien in aliens.sprites(): #Calls each alien in the "sprites list", aliens
        alien.rect.y += ai_settings.fleet_drop_speed #Moves down the amount defined in fleet drop speed
    ai_settings.fleet_direction *= -1 #After it drops, it makes it go the opposite direction (re-stores the value)

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Updating aliens and checking for collisions b/w alien and ship"""
    check_fleet_edges(ai_settings,aliens) #Checks if it hit an edge. If so, drops and changes direction
    aliens.update() #moves each alien in the group right or left

    #Looking for alien-ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)

    #Checking if ship hit bottom of screen
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Responds to a ship being hit by an alien or an alien hitting the bottom"""
    
    if stats.ships_left > 0 : #If the player still has remaining lives...
        #Taking a life away
        stats.ships_left -= 1

        #Playing life lost sound
        lose_ship_sound = pygame.mixer.Sound('ship_lost.wav')
        lose_ship_sound.play()

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Update scoreboard
        sb.prep_ships()

        #Create a new fleet and center the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #Pauses the game once you lose a life
        sleep(0.5)
    
    #If there's no remaining lives:
    else:
        #Stop music then play game over sound
        pygame.mixer.music.stop()
        game_over_sound = pygame.mixer.Sound('game_over.wav')
        game_over_sound.play()

        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Checks if an alien has hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    
    #Treating an alien hitting the bottom like an alien hitting the ship.
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break #Breaks out of the FOR loop

def check_high_score(stats,sb):
    """Check and see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()




















