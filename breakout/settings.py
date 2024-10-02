class Settings:
    """Stores all the settings for the Breakout game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = "black"

        # Ball settings
        self.ball_speed = 2

        # Paddle settings
        self.paddle_speed = 20

        # Brick settings
        self.brick_colors = ["red", "orange", "green", "blue"]