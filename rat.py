import pygame #Lets us work with pygame

class Rat(object):
    """Draws a rat in the center of the screen"""
    def __init__(self,screen):
        """Initializes rat and starting position"""
        self.screen = screen

        #Loads the rat image and initializes its "rect"
        self.image = pygame.image.load('images/rat.bmp') #Loads rat from the images folder
        self.rect = self.image.get_rect() #Creates rat's rect (Like its in game figure)
        self.screen_rect = screen.get_rect() #Creates screen figure (might not need this cuz its already initialized in the Ship class?)

        #Starts each new ship in the middle of the screen
        self.rect.centerx = self.screen_rect.centerx #Puts the center of the rat's rect on the y axis on the screen's rect
        self.rect.centery = self.screen_rect.centery #Puts the center of the rat's rect on the x axis of the screen's rect
    def blitme(self):
        """Allows the rat to be redrawn in its updated location"""
        self.screen.blit(self.image,self.rect) 


