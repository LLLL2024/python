from turtle import Turtle
import random

tim = Turtle()
colors = ["dark orange", "light salmon", "crimson", "light coral", "light pink", "lavender blush", "red", "green", "black", "blue", "pink", "yellow", "forest green"]

def draw_shap(number_of_angles):
     angles = 360 / number_of_angles
     for _ in range(number_of_angles):
         tim.forward(100)
         tim.right(angles)

for shap_side in range (3,12):
    tim.color(random.choice(colors))
    draw_shap(shap_side)