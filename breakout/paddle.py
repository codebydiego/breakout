import turtle

class Paddle:
    """Represents the paddle controlled by the player."""

    def __init__(self):
        """Initializes the paddle's appearance and starting position."""
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_left(self):
        """Moves the paddle to the left if within screen boundaries."""
        x = self.paddle.xcor()
        if x > -350:
            self.paddle.setx(x - 20)

    def move_right(self):
        """Moves the paddle to the right if within screen boundaries."""
        x = self.paddle.xcor()
        if x < 350:
            self.paddle.setx(x + 20)
