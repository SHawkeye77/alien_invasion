#Making the rocket for exercise 12-3. We will:
#1. Add the rocket to the center of the screen
#2. Allow the player to move the rocket up, down, left, or right.
#3. Make sure the rocket can't go beyond any edge of the screen

import pygame #Lets us work with pygame

class Rocket(object):
    """Manages most of the behaviour of the rocket"""
    
    def __init__(self,ai_settings,screen):
        """Initializes the ship and its starting position"""
        self.screen = screen #The screen we draw the rocket on is the same as the screen defined in the initialization of the run_game function
        self.ai_settings = ai_settings #Giving rocket access to ai_settings as an attribute

        #Loads the rocket image and makes its rect
        self.image = pygame.image.load('images/rocket.bmp') #loads rocket image
        self.rect = self.image.get_rect() #Creates rocket's rect
        self.screen_rect = screen.get_rect() #Stores screen's rect as an attribute

        #Starting the rocket in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #Creating center attributes that take decimal values cuz the rect can't
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Creating movement flags (starting stationary)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updates position of rocket based on movement tags"""
        if self.moving_right and self.rect.right < self.screen_rect.right: #Ship moves right if flag is true and its not already at right of the screen
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0: #Ship moves left if flag is true and its not already at left of the screen
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0: #Ship moves up if flag is true and its already not at top of screen
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: #Ship moves right if flag is true and its not already at bottom of screen
            self.centery += self.ai_settings.ship_speed_factor

        #Now we update the actuall rocket position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
            #Redraws rocket to updated location
            self.screen.blit(self.image,self.rect)





