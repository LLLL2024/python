from turtle import Turtle

dotted_line = Turtle()
for _ in range(15):
    dotted_line.forward(10)
    dotted_line.penup()
    dotted_line.forward(10)
    dotted_line.pendown()

