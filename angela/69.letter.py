import random
word_list = ["cat", "dog", "run","angela"]
chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

display = []
for _ in range(length):
    display += "_"
print(display)

end_game = False

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