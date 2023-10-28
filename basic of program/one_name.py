#1
name = input("please enter your name\n")
print("hello," + name + "!")

#2
import math
number = math.pi
circle_radius= float(input("plase enter circle radius\n"))
circle_area = circle_radius ** 2 * number
print(f"circle area: {circle_area:.2f}")


#3

length = float(input("please enter rectangle length\n"))
width = float(input("plase enter rectangle width\n"))

perimter = length * 2 + width * 2
area = length * width
print(f"perimter:{perimter:.10f},area:{area:.10f}")


#4
from decimal import Decimal
number_1 = float(Decimal(input("please enter a number\n")))
number_2 = float(Decimal(input("please enter a number\n")))
number_3 = float(Decimal(input("please enter a number\n")))

sums = (number_1 + number_2 + number_3)
product = (number_1 * number_2 * number_3)
average = sums / 3
print(f"sum: {sums} , product: {product:.6f},   average, {average:.6f}")


#5
talent = float(input("please enter talents\n"))
pound = float(input("please enter pounds\n"))
lot = float(input("please enter lots\n"))

total = talent * 20 * 32 * 13.3 + pound * 32 * 13.3 + lot * 13.3
kilogram = total//1000
gram = total % 1000

formatted = f"The weight in modern units: {kilogram} kilograms and {gram:.2f}grams."
print(formatted)

