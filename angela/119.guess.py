#1.写一个开始游戏字符和猜数字范围
#打印字符串
#随机生成一个函数
# Welcome to the Number Guessing Game!
#I'm thinking of a number between 1 and 100.
import random
from art import logo
hard_number_of_guesses = 5
easy_number_of_guesses = 10


#2.选择模式：困难或者容易
#困难模式猜5次，容易模式猜10次
#写一个选择函数
def comparison(guess,answer,tran):
    """"check answer against guesses. return  turn number of remaining"""
    if guess > answer:
        print("Too high")
        return tran -1

    elif guess < answer:
        print("Too low")
        return tran -1
    else:
        print(f"Pssst, the correct answer is {answer}")


tran = 0
def set_diffcult():
    select_mode = input("Choose a difficulty. Type'hard' and 'easy':")
    if select_mode == "hard":
        return hard_number_of_guesses
    elif select_mode == "easy":
        return easy_number_of_guesses
    print(f"You have {tran} attempts remaining to guess the number.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    tran = set_diffcult()
#3，写一个猜字函数
#如果猜不对就扣一次机会，再循环猜，直到次数全部用完
#
    guess = 0
    while guess != answer:
        print(f"You have {tran} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        tran = comparison(guess, answer, tran)
        if tran == 0 :
            print("you lose,You've run out of guesses")
            return
        elif tran == answer:
            print("guesses again")


game()
#4.开头要显示出logo，
#
#
#
#
#
