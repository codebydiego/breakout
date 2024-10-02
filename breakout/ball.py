import turtle

class Ball:
    """Handles the ball's movement and collision detection in the game."""
    
    def __init__(self):
        """Initializes the ball's appearance and starting position."""
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.speed(0)
        self.ball.goto(0, -200)
        self.ball.dx = 2  # Horizontal velocity
        self.ball.dy = 2  # Vertical velocity

    def move(self):
        """Moves the ball and bounces it off the screen edges."""
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        # Bounce off left and right edges
        if self.ball.xcor() > 390 or self.ball.xcor() < -390:
            self.ball.dx *= -1

        # Bounce off top edge
        if self.ball.ycor() > 290:
            self.ball.dy *= -1

    def check_collision(self, paddle, bricks):
        """Checks for collisions with the paddle or bricks.
        
        Args:
            paddle (Paddle): The paddle object to check collision with.
            bricks (list): A list of Brick objects to check collision with.

        Returns:
            bool: True if a brick is hit, False otherwise.
        """
        # Collision with paddle
        if (self.ball.ycor() > -240 and self.ball.ycor() < -230) and \
           (paddle.paddle.xcor() - 50 < self.ball.xcor() < paddle.paddle.xcor() + 50):
            self.ball.dy *= -1

        # Reset ball if it falls below the screen (bottom edge)
        if self.ball.ycor() < -290:
            self.ball.goto(0, -200)
            self.ball.dy *= -1

        # Collision with bricks
        for brick in bricks:
            if self.ball.distance(brick.brick) < 50:
                self.ball.dy *= -1
                brick.brick.hideturtle()  # Hide the brick when hit
                bricks.remove(brick)  # Remove the brick from the list
                return True
        return False
