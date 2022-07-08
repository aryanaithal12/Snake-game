import turtle
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 0

    def update_score(self):
        self.number += 1

    def write_score(self):
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        style = ('Arial', 15, 'italic')
        self.write(arg=f"Score: {self.number}", font=style, move=False, align='center')

    def clear_score(self):
        self.clear()

    def game_over(self):
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.color('white')
        tim.write(arg=f'GAME OVER! Score: {self.number}', font=('Arial', 20, 'bold'), move=False, align='center')
