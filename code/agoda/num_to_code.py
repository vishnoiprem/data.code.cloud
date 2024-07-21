
# Convert the given Number to a Code and vice-versa

# A number can only be in the range of 1 to 190. A number can be transformed to code "xy" such that x is in range [A, S] and y is in range [0,9] and is in increasing order.
# For example:
#
# | Number |  Code  |
# | 1      |  A0    |
# | 2      |  A1    |
# | 11     |  B0    |
# | 100    |  J9    |
# | 190    |  S9    |
# Implement function to get Code with given number
# f(100) = "J9"
#
# Implement function to get number with given code
# f("J9") = 100


def number_to_code(number):
    if number < 1 or number > 190:
        raise ValueError("Number out of range")

    letters = "ABCDEFGHIJKLMNOPQRS"
    quotient = (number - 1) // 10
    remainder = (number - 1) % 10

    return f"{letters[quotient]}{remainder}"


def code_to_number(code):
    if len(code) != 2 or not ('A' <= code[0] <= 'S') or not ('0' <= code[1] <= '9'):
        raise ValueError("Invalid code format")

    letters = "ABCDEFGHIJKLMNOPQRS"
    letter_value = letters.index(code[0])
    digit_value = int(code[1])

    return letter_value * 10 + digit_value + 1


# Testing the functions
print(number_to_code(100))  # Output should be "J9"
print(code_to_number("J9"))  # Output should be 100
