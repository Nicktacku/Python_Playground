# uno game
import time
import random
import string
import colorama
from colorama import Fore, Back, Style


colorama.init(autoreset=True)


# draws a card by getting a random value
# from the deck and removing the chosen value
# from the list
def draw():
    drawn = random.choice(cards)
    cards.remove(drawn)
    return drawn


# turns the inputted letter into number
# by for looping the alphabet list and
# adding the counter till it matches the letter
def equivalent(letter):
    counter = -1
    for i in alphabet:
        counter += 1
        if i == letter:
            return counter


# checks color of played and past card
# if the name is both seen it will
# return true
def color_comparer(pm, pc):

    if "red" in pc:
        return "red" in pm

    elif "blue" in pc:
        return "blue" in pm

    elif "green" in pc:
        return "green" in pm

    elif "yellow" in pc:
        return "yellow" in pm


# checks if the number is in player
# move and player card by
def number_comparer(pm, pc):
    space_loc = 0

    # the color detected will give a different
    # scpace loc where they will locate the number
    # starting there to scan the pc or pm because of
    # colorama adds different more numbers
    for i in range(10):
        if "red" in pc:
            space_loc = 5
        elif "blue" in pc:
            space_loc = 18
        elif "green" in pc or "yellow" in pc:
            space_loc = 14
        if str(i) in pc[space_loc:] and "+2" not in pc[space_loc:]:
            if "red" in pm:
                space_loc = 6
            elif "blue" in pm:
                space_loc = 18
            elif "green" in pm or "yellow" in pm:
                space_loc = 12
            return str(i) in pm[space_loc:] and "+2" not in pm[space_loc:]

    if "skip" in pc:
        return "skip" in pm

    elif "reverse" in pc:
        return "reverse" in pm

    elif "+2" in pc:
        return "+2" in pm
    else:
        print("nope")


def player_turn(hm, pm, pc, pcb):
    if hm:
        if pm not in black_cards and (
            color_comparer(pm, pc) or number_comparer(pm, pc)
        ):
            played_card = pm
            player_hand.remove(pm)
            print("played card:", played_card)
            return pm

        elif pm in black_cards:
            available_choices = ["a", "b", "c", "d"]
            new_color = None
            played_card = pm
            player_hand.remove(pm)
            print("played card:", played_card)
            show_current_hand()
            while new_color not in available_choices:
                new_color = input(
                    "\nColor Choices:\na) red\nb) blue\nc) green\nd) yellow\n\nPick letter of the the new color: "
                )
            print("color picked:", change_color(new_color))
            return change_color(new_color)

        else:
            print("card has no match")
            return "mismatch"
    else:
        player_hand.append(draw())
        if has_move(player_hand, pc):
            played_card = player_hand.pop()
            print(played_card, "\n")
            return played_card
        show_current_hand()


def show_current_hand():
    counter = -1
    print("\nCurrent Cards: \n")
    for i in player_hand:
        counter += 1
        print(f"{alphabet[counter]}) {player_hand[counter]}")


# if its add atleast 1 then the player
# has a move
def has_move(ph, pc):
    space_loc = 0
    ctr = 0
    if pc is not None:
        for i in ph:
            space_loc = 0
            if "red" in pc:
                if "red" in i:
                    ctr += 1

            elif "blue" in pc:
                if "blue" in i:
                    ctr += 1

            elif "green" in pc:
                if "green" in i:
                    ctr += 1

            elif "yellow" in pc:
                if "yellow" in i:
                    ctr += 1

            if "skip" in pc:
                if "skip" in i:
                    ctr += 1

            if "reverse" in pc:
                if "reverse" in i:
                    ctr += 1

            if "+2" in pc:
                if "+2" in i:
                    ctr += 1

            if i in black_cards:
                ctr += 1

            for j in range(10):
                if "red" in pc:
                    space_loc = 5
                elif "blue" in pc:
                    space_loc = 18
                elif "green" in pc or "yellow" in pc:
                    space_loc = 14
                if str(j) in pc[space_loc:] and "+2" not in pc[space_loc:]:
                    if "red" in i:
                        space_loc = 6
                    elif "blue" in i:
                        space_loc = 18
                    elif "green" in i or "yellow" in i:
                        space_loc = 12
                    if str(j) in i[space_loc:] and "+2" not in i[space_loc:]:
                        ctr += 1

    if ctr > 0:
        return True
    return False


def next_turn(ct, to, is_reverse=False):
    if is_reverse:
        if ct == to[0]:
            return to[3]
        elif ct == to[1]:
            return to[0]
        elif ct == to[2]:
            return to[1]
        elif ct == to[3]:
            return to[2]
    else:
        if ct == to[0]:
            return to[1]
        elif ct == to[1]:
            return to[2]
        elif ct == to[2]:
            return to[3]
        elif ct == to[3]:
            return to[0]


def opponent_move(hm, oh, pc):
    if hm:
        space_loc = 0
        for i in oh:
            space_loc = 0
            if "red" in pc:
                if "red" in i:
                    played_card = i
                    oh.remove(i)
                    return i

            elif "blue" in pc:
                if "blue" in i:
                    played_card = i
                    oh.remove(i)
                    return i

            elif "green" in pc:
                if "green" in i:
                    played_card = i
                    oh.remove(i)
                    return i

            elif "yellow" in pc:
                if "yellow" in i:
                    played_card = i
                    oh.remove(i)
                    return i

            elif "skip" in pc:
                # do a skip function
                if "skip" in i:
                    played_card = i
                    oh.remove(i)
                    return i

            elif "reverse" in pc:
                # do a reverse function
                if "reverse" in i:
                    played_card = i
                    oh.remove(i)
                    return i

            elif "+2" in pc:
                # do a reverse function
                if "+2" in i:
                    played_card = i
                    oh.remove(i)
                    return i

            if i in black_cards:
                print("\nplayed card:", i)
                color_choices = (
                    [Back.RED + " red "]
                    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue "]
                    + [Fore.BLACK + Back.GREEN + " green "]
                    + [Fore.BLACK + Back.YELLOW + " yellow "]
                )
                played_card = color_choices[random.randint(0, 3)]
                oh.remove(i)
                return played_card

            for j in range(10):
                if "red" in pc:
                    space_loc = 5
                elif "blue" in pc:
                    space_loc = 18
                elif "green" in pc or "yellow" in pc:
                    space_loc = 14
                if str(j) in pc[space_loc:] and "+2" not in pc[space_loc:]:
                    if "red" in i:
                        space_loc = 6
                    elif "blue" in i:
                        space_loc = 18
                    elif "green" in i or "yellow" in i:
                        space_loc = 12
                    if str(j) in i[space_loc:] and "+2" not in i[space_loc:]:
                        oh.remove(i)
                        return i


def change_color(letter_choice):
    if letter_choice == "a":
        return Back.RED + " red "
    elif letter_choice == "b":
        return Style.DIM + Back.BLUE + Fore.BLACK + " blue "
    elif letter_choice == "c":
        return Fore.BLACK + Back.GREEN + " green "
    elif letter_choice == "d":
        return Fore.BLACK + Back.YELLOW + " yellow "


def time_decision():
    return random.uniform(0.5, 1.5)


player_hand = []
player2_hand = []
player3_hand = []
player4_hand = []
played_card = []
discard_pile = []
counter = -1
player_move = ""
num_loc_pc = ""
num_loc_pm = ""
turn_order = []
turn_place = -1
turns = ["1", "2", "3", "4"]
current_turn = ""
istrue = True
reverse_turn = False
add2 = False
add4 = False
drawiteration = 0
has_won = False
alphabet = string.ascii_lowercase


# turn order
for i in range(4):
    turn_place += 1
    turn_order.append(random.choice(turns))
    turns.remove(turn_order[turn_place])

# initialization of lists
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

red_cards = (
    [Back.RED + " red 0 "]
    + [Back.RED + " red 1 "] * 2
    + [Back.RED + " red 2 "] * 2
    + [Back.RED + " red 3 "] * 2
    + [Back.RED + " red 4 "] * 2
    + [Back.RED + " red 5 "] * 2
    + [Back.RED + " red 6 "] * 2
    + [Back.RED + " red 7 "] * 2
    + [Back.RED + " red 8 "] * 2
    + [Back.RED + " red 9 "] * 2
    + [Back.RED + " red +2 "] * 2
    + [Back.RED + " red skip "] * 2
    + [Back.RED + " red reverse "] * 2
)

blue_cards = (
    [Style.DIM + Back.BLUE + Fore.BLACK + " blue 0 "]
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 1 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 2 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 3 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 4 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 5 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 6 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 7 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 8 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 9 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue +2 "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue skip "] * 2
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue reverse "] * 2
)

green_cards = (
    [Fore.BLACK + Back.GREEN + " green 0 "]
    + [Fore.BLACK + Back.GREEN + " green 1 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 2 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 3 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 4 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 5 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 6 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 7 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 8 "] * 2
    + [Fore.BLACK + Back.GREEN + " green 9 "] * 2
    + [Fore.BLACK + Back.GREEN + " green +2 "] * 2
    + [Fore.BLACK + Back.GREEN + " green skip "] * 2
    + [Fore.BLACK + Back.GREEN + " green reverse "] * 2
)

yellow_cards = (
    [Fore.BLACK + Back.YELLOW + " yellow 0 "]
    + [Fore.BLACK + Back.YELLOW + " yellow 1 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 2 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 3 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 4 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 5 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 6 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 7 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 8 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow 9 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow +2 "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow skip "] * 2
    + [Fore.BLACK + Back.YELLOW + " yellow reverse "] * 2
)

# made so that wild cards cant be played first in reference
colored_cards = red_cards + blue_cards + green_cards + yellow_cards

black_cards = [
    f"{Fore.RED}W{Fore.BLUE}i{Fore.YELLOW}l{Fore.GREEN}d{Fore.RESET} Card"
] * 4 + [f"{Fore.RED}W{Fore.BLUE}i{Fore.YELLOW}l{Fore.GREEN}d{Fore.RESET} Card +4"] * 4

cards = red_cards + blue_cards + green_cards + yellow_cards + black_cards

all_cards = cards.copy()


# start of process

# initialization
played_card = draw()
played_card_backup = played_card

while played_card not in colored_cards:
    played_card = draw()

for i in range(7):
    player_hand.append(draw())
    player2_hand.append(draw())
    player3_hand.append(draw())
    player4_hand.append(draw())

print("Uno Game\n\n")

# mechanics
print("Mechanics: Choose the letter of the card you want to play\n")
print("Starting card:", played_card, "\n")

turn = turn_order[0]

while istrue:
    if turn == "1" and has_won is False:
        time.sleep(time_decision())
        print("\n*****************************************************")
        print("Your Turn")
        print("\ninitial card:", played_card)
        hm = has_move(player_hand, played_card)
        if hm:
            show_current_hand()
            move = input("\nEnter Move: ")
            for i in move:
                while i in numbers:
                    move = input("\nWrong input, Enter move again: ")
                    i = move
                break
            while equivalent(move) >= len(player_hand) or equivalent(move) <= -1:
                move = input("\nWrong input, enter move again: ")
            player_move = player_hand[equivalent(move)]
            played_card = player_turn(hm, player_move, played_card, played_card_backup)

            # when card doesnt match
            while played_card == "mismatch":
                move = input("\nEnter Move: ")
                for i in move:
                    while i in numbers:
                        move = input("\nWrong input, Enter move again: ")
                        i = move
                    break
                while equivalent(move) >= len(player_hand) or equivalent(move) <= -1:
                    move = input("\nWrong input, enter move again: ")
                player_move = player_hand[equivalent(move)]
                played_card = player_turn(
                    hm, player_move, played_card, played_card_backup
                )

            if played_card is None:
                played_card = played_card_backup
                print("\n", played_card)

        else:
            player_hand.append(draw())
            if reverse_turn is True:
                reverse_turn = False

            if has_move(player_hand, played_card):
                played_card = player_hand.pop()
                print("\nPlayed card:", played_card)
            else:
                show_current_hand()
                if played_card is None:
                    played_card = played_card_backup
                print("\nYou cant play anything")

        if len(cards) < 1:
            cards += all_cards

        if add2 and "+2" not in played_card:
            for i in range(drawiteration):
                player_hand.append(draw())
            add2 = False
            drawiteration = 0

        if add4 and "+4" not in played_card:
            for i in range(drawiteration):
                player_hand.append(draw())
            add4 = False
            drawiteration = 0

        if "reverse" in played_card:
            if reverse_turn is True:
                reverse_turn = False
            elif reverse_turn is False:
                reverse_turn = True
        elif "skip" in played_card:
            if reverse_turn is False:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn + 1 >= 4:
                    turn = turn_order[0]
                else:
                    turn = turn_order[place_of_turn + 1]
            elif reverse_turn is True:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn - 1 <= -1:
                    turn = turn_order[3]
                else:
                    turn = turn_order[place_of_turn - 1]
        elif "+2" in played_card:
            add2 = True
            drawiteration += 2

        elif "+4" in played_card:
            add4 = True
            drawiteration += 4

        turn = next_turn(turn, turn_order, reverse_turn)

        if len(player_hand) <= 0:
            has_won = True

    if len(cards) < 1:
        cards += all_cards.copy

    # opponent 2 move
    elif turn == "2" and has_won is False:
        time.sleep(time_decision())
        print("\n*****************************************************")
        print("Greg's Turn")
        print("\nLast Card:", played_card)
        print(f"\nGreg cards: {len(player2_hand)}")
        if has_move(player2_hand, played_card):
            played_card = opponent_move(has_move, player2_hand, played_card)
            time.sleep(time_decision())
            print("\ngreg move:", played_card)
            if played_card is None:
                played_card = played_card_backup
        else:
            player2_hand.append(draw())
            if reverse_turn is True:
                reverse_turn = False
            for i in player2_hand:
                if has_move(i, player2_hand):
                    played_card = player2_hand.pop()
                    time.sleep(time_decision())
                    print("Greg's move:", played_card, "\n")
            if played_card is None:
                played_card = played_card_backup
            print("Greg cant play anything")

        if len(cards) < 1:
            cards += all_cards

        if add2 and "+2" not in played_card:
            for i in range(drawiteration):
                player2_hand.append(draw())
            add2 = False
            drawiteration = 0

        if add4 and "+4" not in played_card:
            for i in range(drawiteration):
                player_hand.append(draw())
            add4 = False
            drawiteration = 0

        if "reverse" in played_card:
            if reverse_turn is True:
                reverse_turn = False
            elif reverse_turn is False:
                reverse_turn = True
        elif "skip" in played_card:
            if reverse_turn is False:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn + 1 >= 4:
                    turn = turn_order[0]
                else:
                    turn = turn_order[place_of_turn + 1]
            elif reverse_turn is True:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn - 1 <= -1:
                    turn = turn_order[3]
                else:
                    turn = turn_order[place_of_turn - 1]
        elif "+2" in played_card:
            add2 = True
            drawiteration += 2

        elif "+4" in played_card:
            add4 = True
            drawiteration += 4

        print("\ngreg cards: ", len(player2_hand))

        turn = next_turn(turn, turn_order, reverse_turn)

        if len(player2_hand) <= 0:
            has_won = True

    if len(cards) < 1:
        cards += all_cards.copy

    # opponent 3 move
    elif turn == "3" and has_won is False:
        time.sleep(time_decision())
        print("\n*****************************************************")
        print("Mikey's Turn")
        print("\nLast Card:", played_card)
        print("\nmikey cards:", len(player3_hand))
        if has_move(player3_hand, played_card):
            played_card = opponent_move(has_move, player3_hand, played_card)
            time.sleep(time_decision())
            print("\nmikey move", played_card)
            if played_card is None:
                played_card = played_card_backup
        else:
            player3_hand.append(draw())
            if reverse_turn is True:
                reverse_turn = False
            for i in player3_hand:
                if has_move(i, player3_hand):
                    played_card = player3_hand.pop()
                    time.sleep(time_decision())
                    print("\nmikey move:", played_card, "\n")
            if played_card is None:
                played_card = played_card_backup
            print("Mikey cant play anything")

        if len(cards) < 1:
            cards += all_cards

        if add2 and "+2" not in played_card:
            for i in range(drawiteration):
                player3_hand.append(draw())
            add2 = False
            drawiteration = 0

        if add4 and "+4" not in played_card:
            for i in range(drawiteration):
                player_hand.append(draw())
            add4 = False
            drawiteration = 0

        if "reverse" in played_card:
            if reverse_turn is True:
                reverse_turn = False
            elif reverse_turn is False:
                reverse_turn = True
        elif "skip" in played_card:
            if reverse_turn is False:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn + 1 >= 4:
                    turn = turn_order[0]
                else:
                    turn = turn_order[place_of_turn + 1]
            elif reverse_turn is True:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn - 1 <= -1:
                    turn = turn_order[3]
                else:
                    turn = turn_order[place_of_turn - 1]
        elif "+2" in played_card:
            add2 = True
            drawiteration += 2

        elif "+4" in played_card:
            add4 = True
            drawiteration += 4

        print(f"\nmikey cards: {len(player3_hand)}")

        turn = next_turn(turn, turn_order, reverse_turn)

        if len(player3_hand) <= 0:
            has_won = True

    if len(cards) < 1:
        cards += all_cards.copy

    # opponent 4 move
    elif turn == "4" and has_won is False:
        time.sleep(time_decision())
        print("\n*****************************************************")
        print("Jorge's Turn")
        print("\nLast Card:", played_card)
        print(f"\njorge cards: {len(player4_hand)}")
        if has_move(player4_hand, played_card):
            played_card = opponent_move(has_move, player4_hand, played_card)
            time.sleep(time_decision())
            print("\njorge move:", played_card)
            if played_card is None:
                played_card = played_card_backup
        else:
            player4_hand.append(draw())
            if reverse_turn is True:
                reverse_turn = False
            for i in player4_hand:
                if has_move(i, player4_hand):
                    played_card = player4_hand.pop()
                    time.sleep(time_decision())
                    print("\nJorge move:", played_card, "\n")
            if played_card is None:
                played_card = played_card_backup
            print("jorge cant play anything")

        if add2 and "+2" not in played_card:
            for i in range(drawiteration):
                player4_hand.append(draw())
            add2 = False
            drawiteration = 0

        if add4 and "+4" not in played_card:
            for i in range(drawiteration):
                player_hand.append(draw())
            add4 = False
            drawiteration = 0

        if "reverse" in played_card:
            if reverse_turn is True:
                reverse_turn = False
            elif reverse_turn is False:
                reverse_turn = True
        elif "skip" in played_card:
            if reverse_turn is False:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn + 1 >= 4:
                    turn = turn_order[0]
                else:
                    turn = turn_order[place_of_turn + 1]
            elif reverse_turn is True:
                order_of_turn = "".join(turn_order)
                place_of_turn = order_of_turn.find(turn)
                if place_of_turn - 1 <= -1:
                    turn = turn_order[3]
                else:
                    turn = turn_order[place_of_turn - 1]
        elif "+2" in played_card:
            add2 = True
            drawiteration += 2

        elif "+4" in played_card:
            add4 = True
            drawiteration += 4

        print(f"\njorge cards: {len(player4_hand)}")

        turn = next_turn(turn, turn_order, reverse_turn)

        if len(player4_hand) <= 0:
            has_won = True

    # terminator
    if (
        len(player_hand) <= 0
        or len(player2_hand) <= 0
        or len(player3_hand) <= 0
        or len(player4_hand) <= 0
    ):
        print("\n*****************************************************")
        if len(player_hand) <= 0:
            print("You Win!")
        elif len(player2_hand) <= 0:
            print("Greg Wins!")
        elif len(player3_hand) <= 0:
            print("Mikey Wins!")
        elif len(player4_hand) <= 0:
            print("Jorge Wins!")
        istrue = False

    if len(cards) < 1:
        cards += all_cards.copy
