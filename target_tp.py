import pygame

class Target(object):
    """Creating a class that makes a target."""
    def __init__(self,ai_settings,screen):
        #Initializing target attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set the dimensions and properties of the target
        self.width, self.height = 75, 200 #Setting the width as 75 and height as 200
        self.target_color = (200,0,0)
        self.text_color = (255,255,255)

        #Creating target rect and centering it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.right = self.screen_rect.right #Lining up the right side of the target with the right side of the screen
        self.rect.centery = self.screen_rect.centery #Centering the y-attribute
    
    #Drawing the target
    def draw_target(self):
        #Draws the target on screen
        self.screen.fill(self.target_color,self.rect)