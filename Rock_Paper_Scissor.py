import random


def play():
    user = input("'r' for rock 'p' for paper 's' for scissor: ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "tie"

    if is_win(user, computer):
        return "You won"

    return "you lost"


def is_win(p, o):
    if (p == "r" and o == "s") or (p == "s" and o == "p")\
            or (p == "p" and o == "r"):
        return True


print(play())
