#Write a function that gets a list of integers as a parameter.
#except that all uneven numbers have been removed.
#print out both the original as well as the cut-down list.
def ins(list):
    n = []
    for i in list:
        end = i % 2
        if end == 0:
            n.append(i)
            print(i)
    return n


number_list = [1,2,3,4,5,6,7,8,9,10]
m = ins(number_list)
print(number_list)
print(m)

#Write a function that receives two parameters:
# the diameter of a round pizza in centimeters
# and the price of the pizza in euros.

def pizza(diameter,prices):
    extent = 3.14 * diameter** 2 /10000
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



#Write a program that asks the user for a number of a month
# and then prints out the corresponding season
season = ("spring","summer","autumn","winter")
month = int(input("enter a number 1- 12\n"))


if 1<= month <= 3:
    print(f"{month}month is {season[0]}")

elif 4 <= month <=6:
    print(f"{month}month is {season[1]}")

elif 7 <= month <= 9:
    print(f"{month}month is {season[2]}")

elif 10<= month <= 12:
    print(f"{month}month is {season[3]}")
