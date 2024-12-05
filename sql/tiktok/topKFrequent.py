import heapq
from collections import Counter


def topKFrequent(nums, k):
    # Step 1: Build frequency map
    count = Counter(nums)

    # Step 2: Use heap to find the k most frequent elements
    return heapq.nlargest(k, count.keys(), key=count.get)


# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]