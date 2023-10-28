from turtle import Turtle
import random
colors = ["dark orange", "light salmon", "crimson", "light coral", "light pink", "lavender blush", "red", "green", "black", "blue", "pink", "yellow", "forest green"]
diretion =[0, 90, 180, 270]
genrate = Turtle()
genrate.pensize(15)
genrate.speed("fastest")

# genrate.color(random.choice(colors))
#
# def direction():
#     genrate.right(90)
#     genrate.left(90)
#
#
# def potion_distance():
#     for distance in range(1,5):
#         genrate.pensize(distance)
for _ in range(200):
    genrate.color(random.choice(colors))
    genrate.forward(30)
    genrate.setheading(random.choice(diretion))