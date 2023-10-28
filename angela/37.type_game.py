game1 = input("Do you want to right or left?")
lower_game1 = game1.lower()

if lower_game1 == "left":
    print("welcome to game2")

    game2 = input("Do you want to swim or wait? ")
    lower_game2 = game2.lower()
    if lower_game2 == "wait":
        print("please find the door.")

        game3 = input("which door?yellow or blue or red?  ")
        lower_game3 = game3.lower()
        if lower_game3 == "yellow":
            print("You win!")
        else:
            print("game over.")
