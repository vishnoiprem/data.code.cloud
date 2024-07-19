
Convert the given Number to a Code and vice-versa

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



def num_to_code(num):

    dict_num = 'abcdefghijklmnopqrst'

    numerator = num//10
    denominator = num%10

    dist_umn=denominator+




