def shipWithinDays(weights, days):
    # Helper function to determine if a given capacity can ship within `days`
    def canShip(capacity):
        days_needed = 1
        total = 0
        for weight in weights:
            if total + weight > capacity:
                days_needed += 1
                total = 0
            total += weight
        return days_needed <= days

    # Binary search to find the minimum ship capacity
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if canShip(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example Usage:
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

# Running the function
min_capacity = shipWithinDays(weights, days)
print(f"Minimum capacity needed to ship within {days} days: {min_capacity}")