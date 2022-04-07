from turtle import Screen
import time
from snake import Snake
from eat import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title(f"Khalit's Snake Game!")

snake = Snake()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.move_up, key='Up')
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right,key="Right")
screen.onkey(fun=snake.move_left,key="Left")

start_game = True

while start_game:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(ball) < 15:
        ball.new_location()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        start_game = False
        score.game_over()

    for sections in snake.segments[1: len(snake.segments)]:
        if snake.head.distance(sections) < 10:
            start_game = False
            score.game_over()


screen.exitonclick()

