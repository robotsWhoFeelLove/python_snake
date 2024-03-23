from turtle import Turtle

high_score = 0

with open("high_score.txt", mode="r") as file:
    contents = file.read()
    if contents:
        high_score = int(contents)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0,280)
        self.score = 0
        self.highscore = high_score
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}",False,align="center", font=('Arial', 14, 'normal'))
    def increment(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!!!", False, align="center", font=('Arial', 14, 'normal'))

    def reset_scoreboard(self):
        self.setposition(0, 280)
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.score}")

        self.score = 0
        self.show_score()

