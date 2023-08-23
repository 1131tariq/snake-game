from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 20, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        with open("/Users/USER/Desktop/data.txt") as data:
            self.high_score = 100
        self.score = 0

    def current_score(self):
        self.clear()
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.write(arg=f"Score: {self.score} High score: {self.high_score} ", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/USER/Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.current_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
