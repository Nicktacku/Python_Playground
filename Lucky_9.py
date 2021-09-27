import random


def lucky():
    first_card = random.randint(1, 10)
    second_card = random.randint(1, 10)
    o_fcard = random.randint(1, 10)
    o_scard = random.randint(1, 10)
    o_tcard = random.randint(1, 10)
    players_cards = []
    opponents_cards = []
    players_cards.append(first_card)
    players_cards.append(second_card)
    opponents_cards.append(o_fcard)
    opponents_cards.append(o_scard)
    replacement = ["K", "J", "Q", "10"]
    p_hand_value = 0
    o_hand_value = 0
    opponent_decision = random.randint(1, 2)
    who_wins = ""

    if first_card == 10:
        players_cards[0] = random.choice(replacement)

    elif second_card == 10:
        players_cards[1] = random.choice(replacement)

    elif first_card and second_card == 10:
        players_cards[0] = random.choice(replacement)
        players_cards[1] = random.choice(replacement)

    if o_fcard == 10:
        opponents_cards[0] = random.choice(replacement)

    elif o_scard == 10:
        opponents_cards[1] = random.choice(replacement)

    elif o_fcard and o_scard == 10:
        opponents_cards[0] = random.choice(replacement)
        opponents_cards[1] = random.choice(replacement)

    o_hand_value = o_fcard + o_scard
    p_hand_value = first_card + second_card

    if o_hand_value > 9:
        o_hand_value -= 10

        if o_hand_value >= 10:
            o_hand_value -= 10

    if p_hand_value > 9:
        p_hand_value -= 10

        if p_hand_value >= 10:
            p_hand_value -= 10

    if opponent_decision == 1:

        if o_hand_value < 7:
            opponents_cards.append(o_tcard)
            o_hand_value += o_tcard

            if o_hand_value > 9:
                o_hand_value -= 10

                if o_hand_value == 10:
                    o_hand_value -= 10

    print(f"\nThis are your cards {players_cards}")
    player_decision = input("do you want another card? \
(Y) or (N) \nEnter: ").lower()

    if player_decision == "y":
        third_card = random.randint(1, 10)
        players_cards.append(third_card)

        if third_card == 10:
            players_cards[2] = random.choice(replacement)

        p_hand_value += third_card

        if p_hand_value > 9:
            p_hand_value -= 10

            if p_hand_value >= 10:
                p_hand_value -= 10

        if p_hand_value > o_hand_value:
            who_wins = "You Win!\n"

        elif p_hand_value < o_hand_value and \
                len(players_cards) >= len(opponents_cards):
            who_wins = "You Lose!\n"

        elif p_hand_value == o_hand_value and \
                len(players_cards) <= len(opponents_cards):
            who_wins = "You Win!\n"

        elif p_hand_value == o_hand_value and \
                len(players_cards) > len(opponents_cards):
            who_wins = "You Lose!\n"

        else:
            who_wins = "It's a tie\n"

        print(f"\nYour cards are {players_cards} it totaled {p_hand_value}")
        print(f"opponent's cards are {opponents_cards}\
 it totaled {o_hand_value}")
        print(who_wins)

    if player_decision == "n":

        if p_hand_value > o_hand_value:
            who_wins = "You Win!"

        elif p_hand_value < o_hand_value:
            who_wins = "You Lose!"

        elif p_hand_value == o_hand_value and \
                len(players_cards) <= len(opponents_cards):
            who_wins = "You Win!"

        elif p_hand_value == o_hand_value and \
                len(players_cards) > len(opponents_cards):
            who_wins = "You Lose!"

        else:
            who_wins = "It's a tie"

        print(f"\nYour cards are {players_cards}\
 it totaled {p_hand_value}")
        print(f"opponent's cards are {opponents_cards}\
 it totaled {o_hand_value}")
        print(who_wins)


lucky()
