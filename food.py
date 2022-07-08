from turtle import Turtle
import snake
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color('blue')
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.goto(x, y)
        self.speed('fastest')

    def refresh(self, snakebody):
        x = random.randint(-290, 280)
        y = random.randint(-290, 280)
        for _ in snakebody:
            while (x - _.xcor()) < 15 and (y - _.ycor()) < 15:
                x = random.randint(-290, 280)
                y = random.randint(-290, 280)
        self.goto(x, y)
