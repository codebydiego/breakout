import turtle
from breakout.paddle import Paddle
from breakout.ball import Ball
from breakout.brick import create_bricks
from breakout.score import Score
from breakout.settings import Settings

class Game:
    """Main game class for the Breakout game."""

    def __init__(self):
        """Initialize the game."""
        self.settings = Settings()
        self.window = self.setup_screen()
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = create_bricks()
        self.score = Score()
        self.setup_controls()

    def setup_screen(self):
        """Setup the game screen."""
        window = turtle.Screen()
        window.title("Breakout")
        window.bgcolor(self.settings.bg_color)
        window.setup(width=self.settings.screen_width, height=self.settings.screen_height)
        window.tracer(0)
        return window

    def setup_controls(self):
        """Setup controls for the paddle."""
        self.window.listen()
        self.window.onkeypress(self.paddle.move_left, "Left")
        self.window.onkeypress(self.paddle.move_right, "Right")

    def play(self):
        """Main game loop."""
        while True:
            self.window.update()  # Refresh screen
            self.ball.move()  # Move the ball

            # Check for collisions with the paddle and bricks
            if self.ball.check_collision(self.paddle, self.bricks):
                self.score.increase_score()

            # If all bricks are destroyed, end the game
            if not self.bricks:
                break
