
from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = {i: 0 for i in range(numCourses)}
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    queue = deque([k for k in indegree if indegree[k] == 0])
    count = 0
    while queue:
        course = queue.popleft()
        count += 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return count == numCourses

# Example:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: True
# Time Complexity: O(N + E)
# Space Complexity: O(N + E)
