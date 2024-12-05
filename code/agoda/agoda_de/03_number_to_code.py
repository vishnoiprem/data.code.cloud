# Function to convert number to code
def number_to_code(n):
    # Calculate the corresponding letter
    letter = chr(ord('A') + (n - 1) // 10)  # 'A' starts at ord value 65
    # Calculate the corresponding position within the group
    position = (n - 1) % 10
    # Return the formatted code
    return f"{letter}{position}"

# Function to convert code back to number
def code_to_number(code):
    # Extract the letter and digit from the code
    letter = code[0]
    digit = int(code[1])
    # Calculate the group number and add the position within the group
    number = (ord(letter) - ord('A')) * 10 + digit + 1
    return number

# Example usage
print(number_to_code(100))   # Output: J9
print(code_to_number("J9"))  # Output: 100