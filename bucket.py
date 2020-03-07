import pygame #Lets us work with pygame

class Bucket(object):
    """Manages most of the behaviour of the player's bucket"""
    
    def __init__(self,ai_settings,screen):
        """Initializes the Bucket and its starting position"""
        self.screen = screen #The screen we draw the bucket on is the same as the screen defined in the initialization of the run_game function
        self.ai_settings = ai_settings #The AI Settings are made as an attribute of the bucket! Done so we can change them locally for the bucket (to alter speed) in update()

        #Loads the bucket image and gets its "rect" (basically like its in-game figure)
        self.image = pygame.image.load('images/bucket.bmp') #Loads the bucket image from the images folder
        self.rect = self.image.get_rect() #Creates bucket's rect
        self.screen_rect = screen.get_rect() #Stores screen's rect as an attribute

        #Start each new bucket at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Creates a "center" attribute for the bucket so we can store a decimal value for the bucket's center...
        #...because we can't store a decimal value directly with the bucket's rect attribute
        self.center = float(self.rect.centerx)

        #Movement flags (At rest to start with)
        self.moving_right = False
        self.moving_left = False 

    def update(self):
        """Updates the bucket's position based on the SHIP's movement tag (for simplicity)"""
        if self.moving_right and self.rect.right < self.screen_rect.right: #bucket is moved right if the flag is True and it is not already at the right of the screen
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 : #bucket moved left if this flag is true and its not already at the complete left of the screen
            self.center -= self.ai_settings.ship_speed_factor

        #Now we update the actual rect (self.center is kinda just a placeholder to handle precise calculations since rect can't work with decimals)
        self.rect.centerx = self.center

    def blitme(self):
            """Redraws the bucket to its updated (current) location"""
            self.screen.blit(self.image,self.rect)
