from turtle import Turtle

DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.body = []
        self.building_a_snake()
        self.head = self.body[0]

    def building_a_snake(self):
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.shape('square')
            new_turtle.color("white")
            new_turtle.penup()
            self.body.append(new_turtle)
        for i in range(1, 3):
            self.body[i].setx(self.body[i - 1].xcor() - 20)

    def move(self):
        for seg_no in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_no - 1].xcor()
            new_y = self.body[seg_no - 1].ycor()
            self.body[seg_no].goto(new_x, new_y)
            self.body[seg_no].setheading(self.body[seg_no - 1].heading())
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add(self):
        new_seg = Turtle()
        new_seg.setheading(self.body[-1].heading())
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        if self.body[-1].heading() == RIGHT:
            new_seg.goto(self.body[-1].xcor() - 20, self.body[-1].ycor())
            self.body.append(new_seg)
        elif self.body[-1].heading() == UP:
            new_seg.goto(self.body[-1].xcor(), self.body[-1].ycor() - 20)
            self.body.append(new_seg)
        elif self.body[-1].heading() == LEFT:
            new_seg.goto(self.body[-1].xcor() + 20, self.body[-1].ycor())
            self.body.append(new_seg)
        elif self.body[-1].heading() == DOWN:
            new_seg.goto(self.body[-1].xcor(), self.body[-1].ycor() + 20)
            self.body.append(new_seg)

    def check(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290:
            return True
        elif self.head.ycor() > 300 or self.head.ycor() < -290:
            return True
        else:
            return False

    def check_self_col(self):
        for _ in self.body:
            if _ == self.head:
                continue
            elif _.distance(self.head) < 15:
                return True
        return False
