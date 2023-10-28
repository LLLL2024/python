#1.选择用户，输入函数
#import the random module
#use randint() to genrate a random integer
#
#2.你赢了加一分，
# 输了后清理屏幕，查看得分，清理方法，
#2.
#打印logo

from art import logo, vs
from game_data import data
from replit import clear
import random


def format_data(account):
    """Takes account data into printable format"""
    account_name = account["name"]
    account_country = account["country"]
    account_descr = account["description"]
    return f"{account_name},a {account_descr}, from{account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
print(logo)
game_sholud_continue = True
account_b = random.choice(data)

while game_sholud_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compareA {format_data(account_a)}.")
    print(vs)
    print(f"compareB {format_data(account_b)}.")

    guess = input("who has more following? type 'A' or 'B'").lower()
    Current_score = 0

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You are right! Current score:{score}")
    else:
        game_sholud_continue = False
        print(f"sorry,that's wrong. Final score:{score}")



