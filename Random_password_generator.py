import random
alpha_num = ["a", "b", "c", "d", "e", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

start = int(input("How many letters(Minimum of 8): "))
result = ""

if start >= 8:
    for i in range(start):
    
        choices = random.choice(alpha_num)
        result += choices

elif start < 8:
    print("the minimum is 8 letters!")

else:
    print("Error")

print(result)