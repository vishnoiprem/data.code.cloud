def reverseParentheses(s):
    # Use a stack to hold the characters and segments
    stack = []

    # Traverse the string
    for char in s:
        if char == '(':
            # Push an empty string to signify a new level of parentheses
            stack.append("")
        elif char == ')':
            # Pop the last segment, which needs to be reversed
            last_segment = stack.pop()[::-1]

            # If there's still something on the stack, add the reversed segment to it
            if stack:
                stack[-1] += last_segment
            else:
                stack.append(last_segment)
        else:
            # Add the character to the top of the stack
            if stack:
                stack[-1] += char
            else:
                stack.append(char)

    # Join all segments in the stack to get the final string
    return "".join(stack)


# Example Usage:
s = "(u(love)i)"
# Running the function
reversed_string = reverseParentheses(s)
print(f"Reversed string after processing parentheses: {reversed_string}")
