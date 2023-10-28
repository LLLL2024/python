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

