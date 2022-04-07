from turtle import Turtle

ORIGINAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in ORIGINAL_POSITIONS:
            self.grow_snake(position)

    def grow_snake(self, position):
        pieces_of_snake = Turtle("square")
        pieces_of_snake.color("blue")
        pieces_of_snake.shapesize(1.2)
        pieces_of_snake.penup()
        pieces_of_snake.goto(position)
        self.segments.append(pieces_of_snake)

    def extend_snake(self):
        self.grow_snake(self.segments[-1].position())

    def move(self):
        for pieces in range(len(self.segments) - 1, 0, -1):
            x_coord = self.segments[pieces - 1].xcor()
            y_coord = self.segments[pieces - 1].ycor()
            self.segments[pieces].goto(x_coord, y_coord)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
