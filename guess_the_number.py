import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry guess again, too high")
    print("Congrats you have guessed the number")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
           guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)??: ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"The computer have guessed your number, {guess}")

computer_guess(50)