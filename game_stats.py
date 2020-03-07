import json

class GameStats(object):
    """Tracks statisticks for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Starting alien invasion in an active state
        self.game_active = False

        #High score should never be reset
        with open('global_high.json') as f_obj:
            global_high = json.load(f_obj)
            self.high_score = global_high

    def reset_stats(self):
        """Initializes statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit #Checks the settings for how many ships we have left
        self.score = 0
        self.level = 1

