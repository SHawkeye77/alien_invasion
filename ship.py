import pygame #Lets us work with pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Manages most of the behaviour of the player's ship"""
    
    def __init__(self,ai_settings,screen):
        """Initializes the ship and its starting position"""
        super(Ship,self).__init__()
        self.screen = screen #The screen we draw the ship on is the same as the screen defined in the initialization of the run_game function
        self.ai_settings = ai_settings #The AI Settings are made as an attribute of the ship! Done so we can change them locally for the ship (to alter speed) in update()

        #Loads the ship image and gets its "rect" (basically like its in-game figure)
        self.image = pygame.image.load('images/ship_blue.bmp') #Loads the ship image from the images folder
        self.rect = self.image.get_rect() #Creates ship's rect
        self.screen_rect = screen.get_rect() #Stores screen's rect as an attribute

        #Start each new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Creates a "center" attribute for the ship so we can store a decimal value for the ship's center...
        #...because we can't store a decimal value directly with the ship's rect attribute
        self.center = float(self.rect.centerx)

        #Movement flags (At rest to start with)
        self.moving_right = False
        self.moving_left = False 

    def update(self):
        """Updates the ship's position based on the movement tag"""
        if self.moving_right and self.rect.right < self.screen_rect.right: #Ship is moved right if the flag is True and it is not already at the right of the screen
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 : #Ship moved left if this flag is true and its not already at the complete left of the screen
            self.center -= self.ai_settings.ship_speed_factor

        #Now we update the actual rect (self.center is kinda just a placeholder to handle precise calculations since rect can't work with decimals)
        self.rect.centerx = self.center

    def blitme(self):
            """Redraws the ship to its updated (current) location"""
            self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx