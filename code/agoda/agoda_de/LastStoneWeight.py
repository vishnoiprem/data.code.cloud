
import heapq

def lastStoneWeight(stones):
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        first = -heapq.heappop(stones)
        second = -heapq.heappop(stones)
        if first != second:
            heapq.heappush(stones, -(first - second))
    return -stones[0] if stones else 0

# Example:
# Input: [2,7,4,1,8,1]
# Output: 1
# Time Complexity: O(N log N)
# Space Complexity: O(N)
