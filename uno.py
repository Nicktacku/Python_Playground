# uno game
import random
import string
import colorama
from colorama import Fore, Back, Style


# notes
# - add +2 in num comparator
colorama.init(autoreset=True)

# initial placeholders
alphabet = string.ascii_lowercase


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
# if the color is in the played card
# if the color red is in player move
# it will return true
def color_comparer(pm, pc):

    if "red" in pc:
        return "red" in pm

    elif "blue" in pc:
        return "blue" in pm

    elif "green" in pc:
        return "green" in pm

    elif "yellow" in pc:
        return "yellow" in pm

    else:
        print("nope")


# checks if the number is in player
# move and player card
def number_comparer(pm, pc):
    space_loc = 0

    # adds the space loc to move through the
    # initial numbers that messing the code
    for i in range(len(pc)):
        space_loc += 1
        if " " == pc[i]:
            break

    for i in range(10):
        if str(i) in pc[space_loc:]:
            return str(i) in pm[space_loc:]

    if "skip" in pc:
        # do a skip function
        return "skip" in pm

    elif "reverse" in pc:
        # do a reverse function
        return "reverse" in pm

    elif "+2" in pc:
        # do a reverse function
        return "+2" in pm
    else:
        print("nope")


# player turn logic
def player_turn(hm, pm, pc):
    if hm:
        move = input("Enter Move: ")
        pm = player_hand[equivalent(move)]

        if color_comparer(pm, pc) or number_comparer(pm, pc):
            played_card = pm
            player_hand.remove(pm)
            print(played_card)
            show_current_hand()
            return pm

        elif pm in black_cards:
            played_card = pm
            player_hand.remove(pm)
            print(played_card)
            show_current_hand()
            return pm

        else:
            print("error")
    else:
        player_hand.append(draw())
        if has_move(pm, pc):
            played_card = player_hand.pop()
            print(played_card, "\n")
        show_current_hand()


def show_current_hand():
    counter = -1
    print("\nCurrent Cards: \n")
    for i in player_hand:
        counter += 1
        print(f"{alphabet[counter]}) {player_hand[counter]}")


def has_move(ph, pc):
    space_loc = 0
    ctr = 0
    print("played card in has move: ", pc)
    for i in ph:
        space_loc = 0
        if "red" in pc:
            if "red" in i:
                ctr += 1
                print("add 1 in red")

        elif "blue" in pc:
            if "blue" in i:
                ctr += 1
                print("add 1 in blue")

        elif "green" in pc:
            if "green" in i:
                ctr += 1
                print("add 1 in green")

        elif "yellow" in pc:
            if "yellow" in i:
                ctr += 1
                print("add 1 in yellow")

        elif "skip" in pc:
            # do a skip function
            if "skip" in i:
                ctr += 1
                print("add 1 in skip")

        elif "reverse" in pc:
            # do a reverse function
            if "reverse" in i:
                ctr += 1
                print("add 1 in skip")

        elif "+2" in pc:
            # do a reverse function
            if "+2" in i:
                ctr += 1
                print("add 1 in +2")

        elif i in black_cards:
            ctr += 1
            print("add 1 in wild card")

        for j in range(10):
            if "red" in pc:
                space_loc = 8
            elif "blue" in pc:
                space_loc = 23
            elif "green" or "yellow" in pc:
                space_loc = 16
            if str(j) in pc[space_loc:] and "+2" not in pc[space_loc:]:
                if "red" in i:
                    space_loc = 8
                elif "blue" in i:
                    space_loc = 23
                elif "green" or "yellow" in i:
                    space_loc = 16
                if str(j) in i[space_loc:]:
                    ctr += 1
                    print("add 1 in", str(j))

    if ctr > 0:
        return True
    return False


def next_turn(ct, is_reverse=False):
    if is_reverse:
        if ct == "1":
            return "4"
        elif ct == "2":
            return "1"
        elif ct == "3":
            return "2"
        elif ct == "4":
            return "3"
    else:
        if ct == "1":
            return "2"
        elif ct == "2":
            return "3"
        elif ct == "3":
            return "4"
        elif ct == "4":
            return "1"


def opponent_move(hm, oh, pc):
    if hm:
        print("played card in opponent: ", pc)
        space_loc = 0
        for i in oh:
            space_loc = 0
            if "red" in pc:
                if "red" in i:
                    played_card = i
                    player2_hand.remove(i)
                    print("greg move", played_card)
                    print("greg cards: ", len(player2_hand))
                    return i

            elif "blue" in pc:
                if "blue" in i:
                    played_card = i
                    player2_hand.remove(i)
                    print("greg move", played_card)
                    print("greg cards: ", len(player2_hand))
                    return i

            elif "green" in pc:
                if "green" in i:
                    played_card = i
                    player2_hand.remove(i)
                    print("greg move", played_card)
                    print("greg cards: ", len(player2_hand))
                    return i

            elif "yellow" in pc:
                if "yellow" in i:
                    played_card = i
                    player2_hand.remove(i)
                    print("greg move", played_card)
                    print("greg cards: ", len(player2_hand))
                    return i

            elif "skip" in pc:
                # do a skip function
                if "skip" in i:
                    played_card = i
                    player2_hand.remove(i)
                    print("greg move", played_card)
                    print("greg cards: ", len(player2_hand))
                    return i

            elif "reverse" in pc:
                # do a reverse function
                if "reverse" in i:
                    played_card = i
                    player2_hand.remove(i)
                    print("greg move", played_card)
                    print("greg cards: ", len(player2_hand))
                    return i

            elif "+2" in pc:
                # do a reverse function
                if "+2" in i:
                    played_card = i
                    player2_hand.remove(i)
                    print("greg move", played_card)
                    print("greg cards: ", len(player2_hand))
                    return i

            for j in range(10):
                if "red" in pc:
                    space_loc = 8
                elif "blue" in pc:
                    space_loc = 23
                elif "green" or "yellow" in pc:
                    space_loc = 16
                if str(j) in pc[space_loc:] and "+2" not in pc[space_loc:]:
                    if "red" in i:
                        space_loc = 8
                    elif "blue" in i:
                        space_loc = 23
                    elif "green" or "yellow" in i:
                        space_loc = 16
                    if str(j) in i[space_loc:]:
                        played_card = i
                        player2_hand.remove(i)
                        print("greg move", played_card)
                        print("greg cards: ", len(player2_hand))
                        return i


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
turns = ["1", '2', "3", "4"]
current_turn = ""

# turn order
for i in range(4):
    turn_place += 1
    turn_order.append(random.choice(turns))
    turns.remove(turn_order[turn_place])

# initialization of lists
red_cards = [Back.RED + " red 0 "] \
    + [Back.RED + " red 1 "] * 2 \
    + [Back.RED + " red 2 "] * 2 \
    + [Back.RED + " red 3 "] * 2 \
    + [Back.RED + " red 4 "] * 2 \
    + [Back.RED + " red 5 "] * 2 \
    + [Back.RED + " red 6 "] * 2 \
    + [Back.RED + " red 7 "] * 2 \
    + [Back.RED + " red 8 "] * 2 \
    + [Back.RED + " red 9 "] * 2 \
    + [Back.RED + " red +2 "] * 2 \
    + [Back.RED + " red skip "] * 2 \
    + [Back.RED + " red reverse "] * 2

blue_cards = [Style.DIM + Back.BLUE + Fore.BLACK + " blue 0 "] \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 1 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 2 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 3 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 4 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 5 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 6 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 7 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 8 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue 9 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue +2 "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue skip "] * 2 \
    + [Style.DIM + Back.BLUE + Fore.BLACK + " blue reverse "] * 2

green_cards = [Fore.BLACK + Back.GREEN + " green 0 "] \
    + [Fore.BLACK + Back.GREEN + " green 1 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 2 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 3 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 4 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 5 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 6 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 7 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 8 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green 9 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green +2 "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green skip "] * 2 \
    + [Fore.BLACK + Back.GREEN + " green reverse "] * 2

yellow_cards = [Fore.BLACK + Back.YELLOW + " yellow 0 "] \
    + [Fore.BLACK + Back.YELLOW + " yellow 1 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 2 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 3 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 4 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 5 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 6 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 7 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 8 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow 9 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow +2 "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow skip "] * 2 \
    + [Fore.BLACK + Back.YELLOW + " yellow reverse "] * 2

# made so that wild cards cant be played first in reference
colored_cards = red_cards + blue_cards + green_cards + yellow_cards

black_cards = [f"{Fore.RED}W{Fore.BLUE}i{Fore.YELLOW}l{Fore.GREEN}d{Fore.RESET} Card"] * 4 \
              + [f"{Fore.RED}W{Fore.BLUE}i{Fore.YELLOW}l{Fore.GREEN}d{Fore.RESET} Card +4"] * 4

cards = red_cards + blue_cards + green_cards + yellow_cards \
    + black_cards

all_cards = cards.copy()


# start of process

# initialization
played_card = draw()

while played_card not in colored_cards:
    played_card = draw()

for i in range(7):
    player_hand.append(draw())
    player2_hand.append(draw())
    player3_hand.append(draw())
    player4_hand.append(draw())

# mechanics
print("Mechanics: ")
print("Current turn order: ", turn_order)
print("player 2 hand: ", len(player2_hand))
print("player 3 hand: ", len(player3_hand))
print("player 4 hand: ", len(player4_hand))

# initial round
print("initial card: ", played_card)

# player move
show_current_hand()
played_card = player_turn(has_move(player_hand, played_card), player_move, played_card)
print(played_card)

# opponent 2 move
print(f"Greg cards: {len(player2_hand)}")
if has_move(player2_hand, played_card):
    played_card = opponent_move(has_move, player2_hand, played_card)
else:
    player2_hand.append(draw())
    print(f"Greg cards: {len(player2_hand)}")
