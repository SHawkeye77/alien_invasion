import pygame #working with pygame 
from pygame.sprite import Sprite #Importing the sprite class

class Star(Sprite):
    """A class to create an star in the fleet"""
    def __init__(self,ai_settings,screen):
        """Initializing star and its starting position"""
        super(Star,self).__init__() #done since this is a child class
        self.screen = screen #Making screen an attribute of the star
        self.ai_settings = ai_settings #making the ai settings an attribute of the star
        
        #Load star image and initialize its rect attribute
        self.image = pygame.image.load('images/star.bmp') #Loading image
        self.rect = self.image.get_rect() #Creating the rect attribute

        #Start each new star near the top left of the screen
        self.rect.x = self.rect.width #The right side of the star will be coordinate of the width
        self.rect.y = self.rect.height #The right side of the star will be coordinate of the height 

        #Store star's exact (decimal) position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the star at the current position"""
        self.screen.blit(self.image,self.rect)
