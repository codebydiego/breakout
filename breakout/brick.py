import turtle
from breakout.settings import Settings


class Brick:
    """Class representing a single brick in the game."""

    def __init__(self, x, y, color):
        """Initialize the brick at a given position with a given color."""
        self.brick = turtle.Turtle()
        self.brick.shape("square")
        self.brick.color(color)
        self.brick.shapesize(stretch_wid=1, stretch_len=2)
        self.brick.penup()
        self.brick.goto(x, y)

def create_bricks():
    """Creates a grid of bricks for the game.

    Returns:
        list: A list of Brick objects arranged in a grid.
    """
    bricks = []
    settings = Settings()
    colors = settings.brick_colors
    
    # Generate 4 rows of bricks, 8 bricks per row
    for row in range(4):
        for col in range(8):
            x = -350 + (col * 100)  # Horizontal separation
            y = 250 - (row * 30)    # Vertical separation
            brick = Brick(x, y, colors[row % len(colors)])
            bricks.append(brick)
    
    return bricks