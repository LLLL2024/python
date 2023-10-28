import random
from turtle import Turtle,Screen


screen = Screen()
screen.setup(width=500, height=400)
use_bet = screen.textinput(title= "Make you bet", prompt= "Which turtle will the race? Enter a color?")
color = ["red", "blue", "purple", "green", "orange", "yellow"]
y_moudle = [100,60,20, -20, -60, -100]
all_turtle = []


for turtle_moudle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_moudle])
    new_turtle.goto(x=-230, y=y_moudle[turtle_moudle])
    all_turtle.append(new_turtle)



is_on_forward = False
if use_bet:
    is_on_forward = True

while is_on_forward:
     for turtle in all_turtle:
         randant_distance = random.randint(0,10)
         turtle.forward(randant_distance)
         if turtle.xcor() > 230:
             is_on_forward = False
             win_color = turtle.pencolor()
             if win_color == use_bet:
                 print(f"You win.{win_color} win")
             else:
                 print(f"you lose. {win_color} win")


screen.exitonclick()