import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_socre):
    if user_score > 21 and computer_socre > 21:
        return "You went over. You lose 😤"
    if user_score == computer_socre:
        return "Draw 🙃"

    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_socre == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_socre > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_socre:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"user card : {user_cards}, user score : {user_score}")
        print(f"computer first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_card = input("Do you  want to draw another card? Type 'yes' or 'no'? ")
            if user_should_card == "yes":
                user_cards.append(deal_card())

            elif user_should_card == "no":
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"user card : {user_cards}, user score : {user_score}")
    print(f"computer first card : {computer_cards},computer score: {computer_score}")
    print(compare(user_score, computer_score))


while input("you want to restart the game? type'n' or 'y'") == "y":
    play_game()