import random
from art import logo

print(logo)
user_cards = []
dealer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def Game():
    while True:
        print(f"Your Cards : {user_cards}")
        print(f"Dealer Cards : {dealer_cards}")
        want_card = input(
            "Would you like to have another card? type 'y' or 'n': ").lower()
        while want_card != "n":
            if want_card == "y":
                user_cards.append(draw_card())
                user_max_value = Max_Value(user_cards)
                print(user_cards)
                print(user_max_value)
                break
            elif want_card != "y" or want_card != "n":
                print("Please type 'y' or 'n'")
        game_rules()


def game_rules():
    if user_max_value > 21:
        print("You loose, your value is higher than 21")
    elif user_max_value == dealer_max_value:
        print("It's a Draw")
    elif dealer_max_value > 21:
        print("You Won, Dealer value is higher than 21")
    elif user_max_value > dealer_max_value:
        print("You Won")
    elif user_max_value < dealer_max_value:
        print("You Lose")


def Max_Value(deck):
    value = 0
    for values in deck:
        value += values
    return value


def draw_card():
    card = random.choice(cards)
    return card


game = input("Want to play a blackjack game?, type 'y' or 'n': ").lower()

while game != "n":
    for _ in range(2):
        user_cards.append(draw_card())
        dealer_cards.append(draw_card())
    user_max_value = Max_Value(user_cards)
    dealer_max_value = Max_Value(dealer_cards)
    if dealer_max_value < 17:
        dealer_cards.append(draw_card())
        dealer_max_value = Max_Value(dealer_cards)
    print(dealer_max_value)
    Game()
    next_game = input("want to play another game?").lower()
    if next_game == "n":
        break
    user_cards = []
    dealer_cards = []
