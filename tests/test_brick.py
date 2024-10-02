import unittest
from breakout.brick import Brick, create_bricks

class TestBrick(unittest.TestCase):
    """Unit tests for the Brick class."""

    def test_brick_creation(self):
        """Test if a brick is created at the correct position with the correct color."""
        brick = Brick(0, 250, "red")
        self.assertEqual(brick.brick.xcor(), 0)
        self.assertEqual(brick.brick.ycor(), 250)
        self.assertEqual(brick.brick.color()[0], "red")

    def test_create_bricks(self):
        """Test if the correct number of bricks are created."""
        bricks = create_bricks()
        self.assertEqual(len(bricks), 32)  # 4 rows * 8 columns of bricks
        self.assertIsInstance(bricks[0], Brick)

if __name__ == "__main__":
    unittest.main()
