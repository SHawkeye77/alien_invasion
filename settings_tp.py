class Settings(object):
    """A class to store all settings for Target Practice"""

    def __init__(self):
        """Initializing attributes for the game's settings"""
        #Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51,153,255)

        #Ship settings:
        self.ship_speed_factor = 25

        #Bullet settings:
        self.bullet_width = 50
        self.bullet_height = 5
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5

        #Target settings:
        self.target_direction = 1 #Works like a flag. 1 represents down, -1 represents up.

        #Missed shots allowed
        self.misses_starting_with = 3

        #Increases the speed of the target by this factor each time it is hit
        self.speedup_scale = 1.2

        #Initializes the dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Resetting (re-initializing) settings that change throughout the game"""
        self.bullet_speed_factor = 30 #Bullet speed
        self.target_speed = 30 #Target's speed

    def increase_speed(self):
        """Increases the speed of target and bullets when a shot is hit."""
        self.target_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
