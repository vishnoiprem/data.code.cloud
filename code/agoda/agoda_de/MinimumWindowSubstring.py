def minimumTotal(triangle):
    # Start from the second last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update each element to be the sum of itself and the minimum of the two elements below it
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

    # The top element now contains the minimum path sum
    return triangle[0][0]


# Example Usage:
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
# Running the function
minimum_path_sum = minimumTotal(triangle)
print(f"Minimum path sum from top to bottom: {minimum_path_sum}")