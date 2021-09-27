import math


def converter():
    decimal_input = float(input("Enter decimal: "))
    list = []
    outcome = ""

    while decimal_input > 0.5:
        decimal = int(decimal_input)
        equivalent = decimal % 2
        decimal_input = math.floor(decimal_input / 2)
        list.append(equivalent)

    for i in list:
        outcome = str(i) + outcome

    print(outcome)


converter()
