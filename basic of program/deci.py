#1.asks a fisher the length of a zander in centimeters.
zander = float(input("a fisher the length/centimeters\n"))
length = zander - 42
if length >= 0:
    print(("It's good."))
else:
   print(f"release the fish back into the lake,below the size limit {length}")

#2. enter the cabin class of a cruise ship
ship_class = input("enter the cabin class of a cruise ship,Lux or A or B or C\n")
if ship_class == "Lux" or "LUX" or "lux":
    print("upper-deck cabin with a balcony.")
elif ship_class == "A" or "a":
    print("above the car deck, equipped with a window.")
elif ship_class == "B" or "b":
    print("windowless cabin above the car deck")
elif ship_class == "C" or "c":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#3. asks for the biological gender and hemoglobin value (g/l).
bilogical = input("female or male\n")
value = float(input("hemoglobin value(g/l).\n"))
if bilogical == "female":
   if value > 155:
       print("your hemoglobin value is too high")
   elif value < 117:
       print("your hemoglobin value is too low")
   else:
       print("your hemoglobin is normal")
elif bilogical == "male":
    if value > 167:
        print("your hemoglobin value is too high")
    elif value < 134:
        print("your hemoglobin value is too low")
    else:
        print("your hemoglobin is normal")

#4
year = int(input("a year\n"))
if year % 4 == 0 and year % 100 != 0:
        print("It's a leap year")
elif year % 400 == 0:
    print("It's a leap year")
else:
    print("It isn't a leap year")


#while
#1.divisible by three
i = 0
while i <= 1000:
    i +=1
    numbers = i % 3
    if numbers == 0:
        print(i)

#2. converts inches to centinmeters
centimeters = float(input("user input a number/ centimeters\n"))
N = True
while centimeters >= 0 :
    if N == True:
        inches = centimeters * 2.54
        print(inches)
        centimeters = float(input("user input a number/ centimeters\n"))


    elif centimeters < 0 :
        N = False
        print("The program ends")


#3. a random integer between 1 and 10
import random
numbers = random.randrange(1,11)
n = True
user = int(input("enter a numbera between 1 and 10\n"))
while n == True:
    if user < numbers:
        print("too low")
        user = int(input("between 1 and 10\n"))
    elif user > numbers:
        print("too high")
        user = int(input("enter a number between 1 and 10\n"))
    elif user == numbers:
        print("correct")
        n = False

