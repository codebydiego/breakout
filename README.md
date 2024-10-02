# Breakout Game in Python using Turtle

This is a basic implementation of the classic Breakout game using Python's Turtle graphics library. The game involves bouncing a ball off a paddle to destroy bricks and gain points.

## Features:
- Simple paddle movement with keyboard input.
- Collision detection between the ball, bricks, and paddle.
- Scoring system for destroyed bricks.
- Multiple levels of bricks with increasing difficulty.

## How to Run:

1. Install Python 3.x.
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the game:
    ```
    python -m breakout.game
    ```

## Project Structure:

- `game.py`: Main game loop and logic.
- `paddle.py`: Paddle class for player control.
- `ball.py`: Ball class with movement and collision logic.
- `brick.py`: Brick class for brick generation and destruction.
- `score.py`: Scoring system.
- `settings.py`: Contains game configurations (screen size, colors, speeds).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
