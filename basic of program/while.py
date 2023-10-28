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


while centimeters > 0 :
    inches = centimeters * 2.54
    N = True
    print(inches)
    centimeters = float(input("user input a number/ centimeters\n"))

if centimeters < 0 :
    print("The program ends")


#3. a random integer between 1 and 10
import random
numbers = random.randrange(10)

n = True
user = int(input("a number\n"))


while n == True:
    if user < numbers:
        print("too low")
        user = int(input("a number\n"))
    elif user > numbers:
        print("too high")
        user = int(input("a number\n"))
    elif user == numbers:
        print("correct")
        n = False