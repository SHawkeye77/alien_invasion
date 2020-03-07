import pygame #working with pygame 
from pygame.sprite import Sprite #Importing the sprite class

class Alien(Sprite):
    """A class to create an alien in the fleet"""
    def __init__(self,ai_settings,screen):
        """Initializing alien and its starting position"""
        super(Alien,self).__init__() #done since this is a child class
        self.screen = screen #Making screen an attribute of the alien
        self.ai_settings = ai_settings #making the ai settings an attribute of the alien
        
        #Load alien image and initialize its rect attribute
        self.image = pygame.image.load('images/alien_blue.bmp') #Loading image
        self.rect = self.image.get_rect() #Creating the rect attribute

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width #The right side of the alien will be coordinate of the width
        self.rect.y = self.rect.height #The right side of the alien will be coordinate of the height 

        #Store alien's exact (decimal) position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the alien at the current position"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect() #Creates the screen's rect
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves the alien left or right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction) #Updating the x attribute we made to move the alien (can use decimals)
        self.rect.x = self.x #Updating the actual x position (can't use decimals)





