import unittest
from breakout.ball import Ball
from breakout.paddle import Paddle
from breakout.brick import Brick

class TestBall(unittest.TestCase):
    """Unit tests for the Ball class."""

    def setUp(self):
        """Set up the test environment."""
        self.ball = Ball()
        self.paddle = Paddle()
        self.brick = Brick(0, 250, "red")
        self.bricks = [self.brick]

    def test_initial_position(self):
        """Test if the ball is initialized at the correct position."""
        self.assertEqual(self.ball.ball.xcor(), 0)
        self.assertEqual(self.ball.ball.ycor(), -200)

    def test_ball_move(self):
        """Test if the ball moves correctly."""
        initial_x = self.ball.ball.xcor()
        initial_y = self.ball.ball.ycor()
        self.ball.move()
        self.assertNotEqual(self.ball.ball.xcor(), initial_x)
        self.assertNotEqual(self.ball.ball.ycor(), initial_y)

    def test_ball_bounces_off_walls(self):
        """Test if the ball bounces off the screen edges."""
        # Simulate the ball hitting the right wall
        self.ball.ball.setx(390)
        self.ball.move()
        self.assertEqual(self.ball.ball.dx, -2)  # Ball should reverse direction

        # Simulate the ball hitting the top wall
        self.ball.ball.sety(290)
        self.ball.move()
        self.assertEqual(self.ball.ball.dy, -2)  # Ball should reverse direction

    def test_collision_with_paddle(self):
        """Test if the ball collides with the paddle and bounces."""
        # Place ball near paddle and simulate collision
        self.ball.ball.sety(-240)
        self.ball.ball.setx(self.paddle.paddle.xcor())
        self.ball.check_collision(self.paddle, self.bricks)
        self.assertEqual(self.ball.ball.dy, 2)  # Ball should bounce upwards

    def test_collision_with_brick(self):
        """Test if the ball collides with a brick and removes it."""
        self.ball.ball.setx(0)
        self.ball.ball.sety(250)
        hit = self.ball.check_collision(self.paddle, self.bricks)
        self.assertTrue(hit)
        self.assertNotIn(self.brick, self.bricks)  # Brick should be removed

if __name__ == "__main__":
    unittest.main()
