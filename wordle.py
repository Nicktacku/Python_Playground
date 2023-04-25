from random_word import RandomWords
import colorama
from colorama import Fore

# TODO: Fix duplicate letters not being correct
# TODO: Create documentation

colorama.init(autoreset=True)

r = RandomWords()
secret_word = r.get_random_word()


while len(secret_word) != 4:
    secret_word = r.get_random_word()

TRIES = 11
answer = None
display = ["_"] * 4

SECRET_WORD_LIST = [letter for letter in secret_word]
answer_list = []

values = []
indexes = []

accurate = []
inaccurate = []

not_correct = answer_list != SECRET_WORD_LIST
has_tries = TRIES > 0

print(secret_word)

while not_correct and has_tries:
    answer_list.clear()
    TRIES -= 1

    print("-------------------------------------------")
    print("Guess: ", end="")
    for letter in display:
        print(letter, end="")
    print()
    print("correct position: ", accurate)
    print("not in correct position: ", inaccurate)

    display = ["_"] * 4
    accurate.clear()
    inaccurate.clear()

    answer = input("Enter word (only 4 letters): ").lower()

    while len(answer) != 4 or answer.isnumeric():
        print()
        print(Fore.RED + "That is an invalid input" + Fore.RESET)
        answer = input("Enter word (only 4 letters): ").lower()

    answer_list = [i for i in answer]

    for word, ans in zip(SECRET_WORD_LIST, answer_list):
        indexes.append(word == ans)

        if ans in SECRET_WORD_LIST:
            values.append(ans)
        else:
            values.append(None)

    for value, index in zip(values, indexes):
        if value is not None and index is True and value not in accurate:
            accurate.append(value)
        elif value is not None and index is False and value not in inaccurate:
            inaccurate.append(value)

    for secret_letter, letter in zip(SECRET_WORD_LIST, accurate):
        if letter in SECRET_WORD_LIST:
            display[SECRET_WORD_LIST.index(letter)] = letter

    for answer_letter, letter in zip(answer_list, inaccurate):
        if letter in answer_list and letter not in accurate:
            display[answer_list.index(letter)] = letter

    # for letter in inaccurate:
    #     if letter in accurate:
    #         while letter in inaccurate:
    #             inaccurate.remove(letter)

    values.clear()
    indexes.clear()
    not_correct = answer_list != SECRET_WORD_LIST
    has_tries = TRIES > 0

if not not_correct and has_tries:
    print()
    print(Fore.GREEN + "Congratulations! You guessed the word")
else:
    print()
    print(
        f"{Fore.RED}Sorry but the word is {Fore.BLUE}{secret_word}{Fore.RED}, You lose!"
    )
