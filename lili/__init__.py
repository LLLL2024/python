import random
word_list = ["cat", "dog", "run","angela"]
chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

display = []
for _ in range(length):
    display += "_"
print(display)

guess = input("Guess a letter").lower()
end_game = False
lives = 6
while lives > 0:
    if guess not in chosen_word:
        wrong = lives - 1

while not end_game:
  guess = input("Guess a letter").lower()
  for position in range(length):
     letter = chosen_word[position]
     if letter == guess:
        display[position] = letter
  print(display)
  if "_" not in display:
    end_game = True
    print("You win")
  if lives == 0:
      end_of_game = True
      print("You lose!")