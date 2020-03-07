#13-1
#Much work done in star.py
#Added the following to game_functions.py
# def create_star(ai_settings,screen,stars,star_number,row_number):
#     """Creates a star and places it in the row"""
#     star = Star(ai_settings,screen) #Creating a star to add to the fleet
#     star_width = star.rect.width #Making a width attribute to use (from the star we just created)
#     star.x = (star_width + 2 * star_number * star_width) #Defining a value the x position of each star...
#     star.rect.x = star.x #...and then actually putting the value into action by assigning it to the rect attribute.
#     star.rect.y = star.rect.height + (2 * star.rect.height * row_number) #Defining y-value of rect leaving a space for an star in between each
#     stars.add(star) #Adding the star to the fleet list
#
# def create_stars(ai_settings,screen,ship,stars):
#     """Creating a grid of stars"""
#     star = Star(ai_settings,screen) #creating a single star
#     number_stars_x = get_number_aliens_x(ai_settings,star.rect.width) #Decides on the number of stars per row by using the same function we do when doing this for aliens
#     number_rows = get_number_rows(ai_settings,star.rect.height,star.rect.height) #Determining number of rows of stars to have
#
#     #Creating fleet of stars:
#     for row_number in range(number_rows): #Making the following row the amount of times calculated by number_rows
#         for star_number in range(number_stars_x): #Will be done equal to the amount of times suggested by number_aliens_x
#             #Create an star and place it in the row.
#             create_star(ai_settings,screen,stars,star_number,row_number)
#
#In alien_invasion.py...
#stars = Group() #Initializing group of stars 
#gf.create_stars(ai_settings,screen,ship,stars)
#Added 'stars' argument to the update_screen function and changed the function accordingly
#       stars.draw(screen) #Redraw the star fleet (in create_stars)
#Imported Star from star in the game_functions.py



#13-2
#We want to shift each star's position by a random amount
#Imported randint from random
#Added randint(-10,10) to star.rect.x and star.rect.y. Could make larger by increasing range!

#13-3
#1. Create grid of raindrops
#2. Make raindrops fall straight down
#Most work done in raindrop.py
#Added raindrop settings to settings
#Added the following to game_functions.py:
# def create_raindrops(ai_settings,screen,ship,raindrops):
#     """Creates full fleet of raindrops"""
#     raindrop = Raindrop(ai_settings,screen)
#     number_raindrops_x = get_number_aliens_x(ai_settings,raindrop.rect.width) #How many columns of raindrops can we have
#     number_rows = get_number_rows(ai_settings,ship.rect.height,raindrop.rect.height) #How many rows of raindrops can we have
#     #Creating the fleet of raindrops:
#     for row_number in range(number_rows):
#         for raindrop_number in range(number_raindrops_x):
#             create_raindrop(ai_settings,screen,raindrops,raindrop_number,row_number)
# def create_raindrop(ai_settings,screen,raindrops,raindrop_number,row_number):
#     """Creates a raindrop and places it"""
#     raindrop = Raindrop(ai_settings,screen)
#     raindrop_width = raindrop.rect.width
#     raindrop.x = (raindrop_width + 2 * raindrop_number * raindrop_width)
#     raindrop.rect.x = raindrop.x
#     raindrop.rect.y = raindrop.rect.height + (2 * raindrop.rect.height * row_number)
#     raindrops.add(raindrop)
# def update_raindrops(raindrops):
#     """Drops the aliens down (No need to move them left and right)"""
#     raindrops.update() #Moves the alien down
#Then made appropriate additions and argument changes to alien_invasion.py

#13-4
#Ill go about this by basically modifying functions from the normal program that make aliens shift when they hit the side
#Added the following in game_functions.py
# def update_raindrops(ai_settings,raindrops,screen):
#     """Drops the aliens down (No need to move them left and right)"""
#     check_raindrop_edges(ai_settings,raindrops,screen) #Checks if the top of the raindrop rect passed the bot of screen and deals appropriately
#     raindrops.update() #Moves the alien down
# def check_raindrop_edges(ai_settings,raindrops,screen):
#     """Moves a row that just cleared the bottom back to the top"""
#     for raindrop in raindrops.sprites(): #Calls each raindrop in the sprites list, aliens
#         if raindrop.check_edges(): #Returns True if the raindrop hit the bottom
#             replace_raindrop(ai_settings,raindrop,raindrops,screen) #Should delete the raindrop at the bottom and create one at top
#             # break ?
# def replace_raindrop(ai_settings,raindrop,raindrops,screen):
#     """Deletes raindrop that dropped below screen then creates rainbow at top"""
#     raindrops.remove(raindrop) #Removes raindrop that left screen
#     screen_rect = screen.get_rect() #Gets a rect for the screen so we can use it
#     new_raindrop = Raindrop(ai_settings,screen) #Creating this new raindrop
#     new_raindrop.rect.x = raindrop.rect.x #Should have the same x position as the raindrop being deleted
#     new_raindrop.rect.bottom = screen_rect.top #New raindrop's bottom is at the top of the screen

#     raindrops.add(new_raindrop) #Adds the new raindrop to our list of raindrops
#To raindrop.py added:
    # def check_edges(self):
    #     """Checks if the top of a raindrop's rect has hit the bottom of the screen"""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.top >= screen_rect.bottom:
    #         return True
#Updated 'update_screen'




#13-5
#All work is self-contained in catch.py,apple.py,bucket.py,apple_bucket_game_functions.py, and a little bit in settings.py

#13-6
#This uses all the programs mentioned in 13.5 and the new 'game_stats_apple_bucket.py'
#We need to keep track of the number of times the player has missed the ball. If it is 3 times, end the game.

















