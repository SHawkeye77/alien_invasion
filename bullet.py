import pygame #working with pygame
from pygame.sprite import Sprite #Importing the Sprite class from the sprite module

class Bullet(Sprite): #format is... 'class ChildClass(ParentClass):'
    """A class that manages bullets fired from the ship"""
    def __init__(self,ai_settings,screen,ship):
        """Creating bullet object at ship's current position, initializing attributes"""
        super(Bullet,self).__init__() #format is... 'super(ChildClass,self).__init__()' ... when working with a class in a class
        self.screen = screen #Initializing the screen attribute

        #Creating the bullet rect starting at (0,0) then setting current position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,ai_settings.bullet_height) #building bullet not based on an image, but by scratch.
        self.rect.centerx = ship.rect.centerx #Positioning the bullet's center x coordinate at the same place as the ships
        self.rect.top = ship.rect.top #Positioning the top of the bullet at the same place as the top of the ship

        #Storing the bullets position as a decimal (cuz rect can't work with decimals)
        self.y = float(self.rect.y)

        #Initializing color and speed factor values
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen"""
        self.y -= self.speed_factor #Updates position of the bullet higher on the screen
        self.rect.y = self.y #Updates the rect position

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect) #Draws the rect on the screen with 'color'






