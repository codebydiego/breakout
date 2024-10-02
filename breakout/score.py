import turtle

class Score:
    """Handles the scoring system in the game."""

    def __init__(self):
        """Initializes the score display."""
        self.score = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.update_score()

    def update_score(self):
        """Updates the score display."""
        self.pen.clear()
        self.pen.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        """Increases the score and updates the display."""
        self.score += 10
        self.update_score()
