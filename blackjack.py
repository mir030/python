import random


def deal_card():
    # returns a random card from the deck
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # random.choice() selects one item from the list randomly
    random_card = random.choice(card_list)
    return random_card


def calculate_score(cards):
    """will take a list of cards and calculate the sum of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif user_score == 0:
        return "Win with a blackjack"
    elif comp_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif comp_score > 21:
        return "Computer went over, you win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards are {user_cards}, you score is {user_score}")
        print(f"Computer's first card is {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"    You final cards {user_cards}, computers final cards {comp_cards}")
    print(compare(user_score, comp_score))


while input("Do you want to play a game of blackjack? y/n: ") == "y":
    play_game()
