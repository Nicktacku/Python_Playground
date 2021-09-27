import random

print("Random Number Generator")
start = int(input("From: "))
to = int(input("To: "))

rand_int = random.randint(start, to + 1)

print(rand_int)