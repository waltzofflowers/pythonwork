import random

# Define the deck of cards
deck = {
    "A1": [1, 11], "A2": 2, "A3": 3, "A4": 4, "A5": 5, "A6": 6, "A7": 7, "A8": 8, "A9": 9, "A10": 10, "AK": 10, "AQ": 10, "AJ": 10,
    "B1": [1, 11], "B2": 2, "B3": 3, "B4": 4, "B5": 5, "B6": 6, "B7": 7, "B8": 8, "B9": 9, "B10": 10, "BK": 10, "BQ": 10, "BJ": 10,
    "C1": [1, 11], "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7, "C8": 8, "C9": 9, "C10": 10, "CK": 10, "CQ": 10, "CJ": 10,
    "D1": [1, 11], "D2": 2, "D3": 3, "D4": 4, "D5": 5, "D6": 6, "D7": 7, "D8": 8, "D9": 9, "D10": 10, "DK": 10, "DQ": 10, "DJ": 10,
}

list_for_one = ["A1", "B1", "C1", "D1"]

total = 0
is_True = True

def cards_to_pick(number_of_cards):
    selected_values = []
    for i in range(number_of_cards):
        card, value = random.choice(list(deck.items()))
        if card in list_for_one:
            value = random.choice(deck[card])
        else:
            value = deck[card]
        selected_values.append(value)
        del deck[card]
    return selected_values

player_cards = cards_to_pick(2)
house_cards = cards_to_pick(1)

total_player = sum(player_cards)
total_house = house_cards[0]

print(f"Your cards: {player_cards}")
print(f"Computer's first card : {house_cards}")

while True:
    if total_player == 21:
        print("Blackjack! You win..!")
        break
    elif total_player > 21:
        print("You total has exceed 21, you lose..!")
        break

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == "y":
        card = cards_to_pick(1)[0]
        player_cards.append(card)
        total_player += card
        print(f"Your cards: {player_cards}")

        if total_player > 21:
            print("You total has exceed 21, you lose..!")
            break

    elif another_card == "n":
        while total_house < 21:
            card1 = cards_to_pick(1)[0]
            house_cards.append(card1)
            total_house += card1
        print(f"Computer's cards: {house_cards}")

        if total_house > 21:
            print("House total has exceeded 21. You win!...")
        elif total_player > total_house:
            print("You win!")
        elif total_player < total_house:
            print("You lose!")
        else:
            print("It's a tie!")

        break