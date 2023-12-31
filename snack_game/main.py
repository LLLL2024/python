from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.title("snack game")
screen.bgcolor("black")
screen.setup(width= 600, height= 600)
screen.tracer(0)

snake= Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
screen.exitonclick()
