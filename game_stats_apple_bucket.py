class GameStats(object):
    """Tracks statisticks for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Starting apple bucket game in an active state
        self.game_active = True

    def reset_stats(self):
        """Initializes statistics that can change during the game"""
        self.lives_left = self.ai_settings.ship_limit #Checks the settings for how many lives we have left (Making this the same as how many ships we have left for simplicity)

