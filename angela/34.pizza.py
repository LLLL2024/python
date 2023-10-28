print("welcome to Python Pizza Deliveries")
size = input("What size pizza do you want?  S or M  or L?  ")
add_pepperoni = input ("Do you want add pepperoni? Y or N ")
add_size = input("What size pepperoni do you want?  S or M?  ")
extra_cheese = input(" Do you want extra cheese?  Y  or N  ")
bill = 0
if size == "S" :
    bill = 15
elif add_size == "M":
    bill = 20
else:
    bill = 2
if add_pepperoni == "Y":
    if add_size == "S":
     bill += 2
    else:
     bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"you bill is ${bill}")