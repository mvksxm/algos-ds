from collections import defaultdict, deque
from typing import List

# TC -> O(V+E)
# SC -> O(V+E)

# Approach (BFS) (Kahn's Algorithm)
# 1) Create a map that would contain keys in a form of the vertices (nodes) and values in a form of the arrays of edges
# # pointing to the child vertices.
# 2) Create an array that would contain vertices as indexes and values as the amount of edges pointing to them.
# 3) Perform a BFS. To the BFS queue and a res array input vertices that have 0 dependencies (0 edges pointing to them).
# On each BFS iteration, when iterating through the children of a particular node in a queue, decrement the amount of dependencies
# for a child by 1. In case if child has an amount of dependencies < 0 -> return [] (it means it was already a part
# of the queue)
# 4) The expected result after the BFS is that all nodes have been visited and have 0 dependencies. If it's
# not the case and dependency_count array contains even a single non-zero value -> return [].
# 5) If all previous checks have been passed -> return res array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        child_map = defaultdict(list)
        dependency_count = [0] * numCourses
        queue = deque()
        res = []

        for prereq in prerequisites:
            child_map[prereq[1]].append(prereq[0])
            dependency_count[prereq[0]] += 1

        for i in range(len(dependency_count)):
            if dependency_count[i] == 0:
                queue.append(i)
                res.append(i)

        if not queue: return []

        while queue:
            left_elem = queue.popleft()
            for child in child_map[left_elem]:
                dependency_count[child] -= 1
                if dependency_count[child] == 0:
                    queue.append(child)
                    res.append(child)
                if dependency_count[child] < 0: return []

        if any(dependency_count): return []
        return res