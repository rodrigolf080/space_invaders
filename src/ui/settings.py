class Settings:
    """A class that stores all the setting for Alien Invasion."""

    def __init__(self):
        """Initialise the game's static settings."""

        # Screen settings
        # 1297x703 = full windowmode
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the alien points speed up
        self.score_scale = 1.5

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialise_dynamic_settings()


    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 3.0
        self.alien_score = 50

        # Fleet direction of 1 represents right and -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and score points."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_score = int(self.alien_score * self.score_scale)

    def easy(self):
        """Duck shooter."""
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.bullets_allowed = 100
        self.bullet_width = 2000
        self.alien_score = 50

    def medium(self):
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 3.0
        self.bullets_allowed = 5
        self.bullet_width = 3
        self.alien_score = 50

    def hard(self):
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 4.0
        self.bullets_allowed = 3
        self.bullet_width = 3
        self.alien_score = 50

    def impossible(self):
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 5.0
        self.bullets_allowed = 1
        self.bullet_width = 1
        self.alien_score = 50



