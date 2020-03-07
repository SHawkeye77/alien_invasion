class Settings(object):
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializing the game's static settings"""
        #Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51,153,255)

        #Ship settings:
        self.ship_limit = 3 #How many "lives" you have

        #Bullet settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5

        #Alien settings:
        self.fleet_drop_speed = 15 #How far the alien swarm will move down when it drops down

        #How quickly the game speeds up each level
        self.speedup_scale = 1.2

        #How quickly the alien point values increase
        self.score_scale = 1.5

        #Restates certain settings every time w
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Resetting (re-initializing) settings that change throughout the game"""
        self.bullet_speed_factor = 10 #Bullet speed
        self.ship_speed_factor = 15 #Ship's speed
        self.alien_speed_factor = 5 #Aliens' horizontal speed
        self.fleet_direction = 1 #Works like a flag. 1 represents right, -1 represents left.

        #Scoring 
        self.alien_points = 50

    def increase_speed(self):
        """Increases speed settings and alien points values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
