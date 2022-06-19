from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()




screen.exitonclick()