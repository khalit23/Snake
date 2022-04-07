from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(1)
        self.penup()
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def new_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
