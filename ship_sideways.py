import pygame #Lets us work with pygame

class ShipSideways(object):
    """Manages most of the behaviour of the player's ship"""
    
    def __init__(self,ai_settings,screen):
        """Initializes the ship and its starting position"""
        self.screen = screen #The screen we draw the ship on is the same as the screen defined in the initialization of the run_game function
        self.ai_settings = ai_settings #The AI Settings are made as an attribute of the ship! Done so we can change them locally for the ship (to alter speed) in update()

        #Loads the ship image and gets its "rect" (basically like its in-game figure)
        self.image = pygame.image.load('images/ship_sideways.bmp') #Loads the sideways ship image from the images folder
        self.rect = self.image.get_rect() #Creates ship's rect
        self.screen_rect = screen.get_rect() #Stores screen's rect as an attribute

        #Start each new ship at the left center of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        #Creates a "center" attribute for the ship so we can store a decimal value for the ship's center...
        #...because we can't store a decimal value directly with the ship's rect attribute
        self.center = float(self.rect.centery)

        #Movement flags (At rest to start with)
        self.moving_up = False
        self.moving_down = False 

    def update(self):
        """Updates the ship's position based on the movement tag"""
        if self.moving_up and self.rect.top > 0: #Ship is moved up if the flag is True and it is not already at the top of the screen
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom : #Ship moved down if this flag is true and its not already at the complete bottom of the screen
            self.center += self.ai_settings.ship_speed_factor

        #Now we update the actual rect (self.center is kinda just a placeholder to handle precise calculations since rect can't work with decimals)
        self.rect.centery = self.center

    def blitme(self):
            """Redraws the ship to its updated (current) location"""
            self.screen.blit(self.image,self.rect)
