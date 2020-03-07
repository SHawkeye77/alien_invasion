import pygame.font #Lets pygame render text to screen

class Button(object):
    def __init__(self,ai_settings,screen,msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set the dimensions and properties of the button
        self.width, self.height = 200, 50 #Setting the width as 200 and height as 50
        self.button_color = (200,0,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48) #Setting the font to be 'None' (default font), size 48.

        #Creating button rect and centering it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #Rendering string as image
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """Turns given msg into a rendered image and centers the text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color) #From the imported pygame methods
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center #Centers the message's rect with the button's rect

    def draw_button(self):
        #Draws the button then the message on screen
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

