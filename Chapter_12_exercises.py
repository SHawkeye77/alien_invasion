#12-1
#In settings.py, changed to self.bg_color = (0,0,230)

#12-2
#Most of the work done in rat.py
#Imported the rat class in alien_invasion.py
    #from rat import Rat
#Initializing the rat surface in the run_game function
    #rat = Rat(screen)
#Changed the screen update to take both ship and rat arguments:
    #gf.update_screen(ai_settings,screen,ship,rat) #Updates images (ship and rat) on the screen and 'flips' (redraws) the screen\
#Added another argument, 'rat' to update_screen in game_functions and added the following in its block:
    #rat.blitme()
#In settings.py, changed self.bg_color to be (48,92,246) to match the rat image

#12-3
#Most of the work done in ship.py
#Imported the rocket class in alien_invasion.py
    #from rocket import Rocket
#Initialized the rocket surface in the run_game function:
    #rocket = Rocket(ai_settings,screen) #Making a rocket from our Rocket class
#Changed the screen_update function so it updated rocket too
#Updated check_events so it checked for events pertaining to rocket too
#In def check_keyup_events and check_keydown_events we added checks for up arrow key and down arrow key
#Added rocket.blitme() to update_screen block
#Added second argument (rocket) to check_events
#Added fourth argument (rocket) to update_screen
#Added rocket as an argument to all the methods in game_functions

#12-4
#Work done in number_game.py

#12-5
#Done in sideways_shooter.py, game_functions_sideways.py, bullet_sideways.py, and ship_sideways.py
