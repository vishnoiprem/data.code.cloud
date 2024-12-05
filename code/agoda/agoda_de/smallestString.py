def smallestString(s):
    # Convert string to a list of characters for easier manipulation
    s = list(s)
    n = len(s)

    # Find the first character greater than 'a'
    for i in range(n):
        if s[i] > 'a':
            # Start modifying from this character
            while i < n and s[i] > 'a':
                s[i] = chr(ord(s[i]) - 1)  # Decrease the character by one
                i += 1
            # Once modification is done, break out
            break

    # If no character was greater than 'a', change the last character to 'z'
    else:
        s[-1] = 'z'

    # Convert the list back to string and return
    return ''.join(s)


# Example Usage:
s = "abcz"
# Running the function
smallest_lexicographical_string = smallestString(s)
print(f"Lexicographically smallest string: {smallest_lexicographical_string}")
