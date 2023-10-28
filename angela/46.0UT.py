rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock, paper,scissors]
user_choice = int(input('what do you choose? "0" or "1" or "2"\n'))
print(game_images[user_choice])
if user_choice >2 or user_choice < 0:
  print("you typed an invalid, you lose")


computer_choice = random.randint(0,2)
print("computer choice: ")
print(game_images[computer_choice])


if user_choice > 2 or user_choice < 0:
  print("you typed an invalid, you lose")
elif user_choice == 0 and  computer_choice == 2:
  print("You win")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif user_choice > computer_choice:
  print("You lose")
elif user_choice < computer_choice:
  print("You win")
elif user_choice == computer_choice:
  print("It's a draw")
else:
  print("you typed an invalid, you lose")
