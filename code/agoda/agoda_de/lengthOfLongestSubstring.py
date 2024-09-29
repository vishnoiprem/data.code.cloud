def lengthOfLongestSubstring(s):
    # Dictionary to keep track of the last index of each character
    char_index = {}
    left = 0
    max_len = 0

    # Iterate over the string with the right pointer
    for right, char in enumerate(s):
        # If the character is already in the dictionary and is within the window
        if char in char_index and char_index[char] >= left:
            # Move the left pointer to the position after the last occurrence of the character
            left = char_index[char] + 1

        # Update the last seen index of the character
        char_index[char] = right

        # Calculate the maximum length of the current window
        max_len = max(max_len, right - left + 1)

    return max_len

# Example Usage:
s = "abcabcdbb"
# Running the function
longest_length = lengthOfLongestSubstring(s)
print(f"Length of the longest substring without repeating characters: {longest_length}")