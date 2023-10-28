print("welcome to the rollercoaster!")
height = int(input("what's your height in cm:"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("your age:"))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7

    elif  age >= 45 and age <= 55:
        bill = 0

    else:
        bill = 12
    want_photo = input("Do you want photo? Y or N? ")
    if want_photo == "Y" :
            bill += 3
    print(f"you bill is ${bill}")

else:
    print ("You can't ride the rollercoaster")

