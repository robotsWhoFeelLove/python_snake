from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def get_random_coord(self):
        num = random.randint(0,14)
        if random.randint(0,1):
            return (num * -20)
        else:
            return (num * 20)

    def refresh(self):
        self.goto(self.get_random_coord(), self.get_random_coord())

    def reset_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

