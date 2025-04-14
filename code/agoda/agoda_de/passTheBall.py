def passTheBall(N, K):
    # Calculate the child who has the ball after K seconds
    return (K % N) + 1

# Example Usage:
N = 5  # Number of children
K = 7  # Seconds elapsed

# Running the function
child_with_ball = passTheBall(N, K)
print(f"The child with the ball after {K} seconds is: {child_with_ball}")