def converter():
    binary_input = input("Enter Binary: ")
    exponent = -1
    total = 0
    power = 0
    array = []

    for i in binary_input:

        array.append(i)

    array.reverse()

    for i in array:
        exponent = exponent + 1

        if i == "1":
            power = 2 ** exponent
            total = power + total

    print(total)


converter()
