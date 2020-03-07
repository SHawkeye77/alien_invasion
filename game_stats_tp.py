class GameStats(object):
    """Tracks statisticks for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Starting alien invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """Initializes statistics that can change during the game"""
        self.misses_left = self.ai_settings.misses_starting_with #Checks the settings for how many ships we have left
