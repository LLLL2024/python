#Write a function that receives two parameters:
# the diameter of a round pizza in centimeters
# and the price of the pizza in euros.

def pizza(diameter,prices):
    extent = (3.14 * diameter* diameter)/10000
    price = prices / extent
    return price

#enter the diameter and price of two pizzas
# and tells the user which pizza provides better value
# for money (which of them has a lower unit price).
first_diameter = float(input("enter diameter of the first pizza in centimeters\n"))
first_price = float(input("enter price of the first pizza in euros\n"))
second_diameter = float(input("enter diameter of the second pizza in centimeters\n"))
second_price = float(input("enter price of the second pizza in euros\n"))


first_pizza = pizza(first_diameter,first_price)
print(f"the price of the first pizza  {first_pizza: .2f}")

second_pizza = pizza(second_diameter,second_price)
print(f"the price of the second pizza {second_pizza: .2f}")


if first_pizza < second_pizza:
    print(f"the price of the first pizza {first_pizza: .2f} has a lower unit price")

elif first_pizza > second_pizza:
    print(f"the price of the second pizza {second_pizza: .2f} has a lower unit price")

elif first_pizza == second_pizza:
    print(f"the price of the first pizza {first_pizza: .2f},"
          f"and the price of the second pizza {second_pizza: .2f} has a equal price")



