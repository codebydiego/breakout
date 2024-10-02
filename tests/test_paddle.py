import unittest
from breakout.paddle import Paddle

class TestPaddle(unittest.TestCase):
    """Unit tests for the Paddle class."""

    def test_move_left(self):
        """Test if the paddle moves left."""
        paddle = Paddle()
        paddle.paddle.setx(0)  # Set paddle's initial position
        paddle.move_left()
        self.assertEqual(paddle.paddle.xcor(), -20)

    def test_move_right(self):
        """Test if the paddle moves right."""
        paddle = Paddle()
        paddle.paddle.setx(0)  # Set paddle's initial position
        paddle.move_right()
        self.assertEqual(paddle.paddle.xcor(), 20)

if __name__ == "__main__":
    unittest.main()
