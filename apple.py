import pygame #working with pygame 
from pygame.sprite import Sprite #Importing the sprite class
from random import randint #letting us have a random element

class Apple(Sprite):
    """A class to create an apple in the fleet"""
    def __init__(self,ai_settings,screen):
        """Initializing apple and its starting position"""
        super(Apple,self).__init__() #done since this is a child class
        self.screen = screen #Making screen an attribute of the apple
        self.ai_settings = ai_settings #making the ai settings an attribute of the apple
        
        #Load apple image and initialize its rect attribute
        self.image = pygame.image.load('images/apple.bmp') #Loading image
        self.rect = self.image.get_rect() #Creating the rect attribute

        #Positioning the apple randomly at the top of the screen
        screen_rect = self.screen.get_rect() #Need to work with certain screen attributes
        furthest_right = screen_rect.right - (self.rect.width) #This is the furthest right the x-coordinate of the top left of the apple should be
        self.rect.x = randint(0,furthest_right) #Stars the apple at a random spot (that is still completely visible) on the screen
        self.rect.y = 1 #Starts the top of the apple just under the top of the screen  

        #Store apple's exact (decimal) position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the apple at the current position"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """Return True if apple is at edge of screen."""
        screen_rect = self.screen.get_rect() #Creates the screen's rect
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves the apple left or right"""
        self.x += (self.ai_settings.apple_speed_factor * self.ai_settings.fleet_direction) #Updating the x attribute we made to move the apple (can use decimals)
        self.rect.x = self.x #Updating the actual x position (can't use decimals)


