import pygame #working with pygame 
from pygame.sprite import Sprite #Importing the sprite class

class Raindrop(Sprite):
    """A class to create a raindrop"""
    def __init__(self,ai_settings,screen):
        """Initializing raindrop and its starting position"""
        super(Raindrop,self).__init__() #done since this is a child class
        self.screen = screen #Making screen an attribute of the raindrop
        self.ai_settings = ai_settings #making the ai settings an attribute of the raindrop
        
        #Load raindrop image and initialize its rect attribute
        self.image = pygame.image.load('images/raindrop.bmp') #Loading image
        self.rect = self.image.get_rect() #Creating the rect attribute

        #Start each new raindrop near the top left of the screen
        self.rect.x = self.rect.width #The right side of the raindrop will be coordinate of the width
        self.rect.y = self.rect.height #The right side of the raindrop will be coordinate of the height 

        #Store raindrop's exact (decimal) position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the raindrop at the current position"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Call this to moves the raindrop down (rather than left and right)"""
        self.rect.y += self.ai_settings.raindrop_speed_factor

