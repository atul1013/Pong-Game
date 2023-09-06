from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def reset_speed(self):
        self.x_move = 5
        self.y_move = 5

    def fast(self):
        self.x_move *= 1.2
        self.y_move *= 1.2

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()