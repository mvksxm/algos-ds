from collections import deque
from typing import List


# Approach: BFS + visited set
# n -> len(isConnected)
# TC -> O(n ^ 2)
# SC -> O(n)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited_set = set()
        res = 0
        q = deque()

        for i in range(len(isConnected)):
            if i in visited_set: continue

            res += 1
            visited_set.add(i)
            q.append(i)

            while q:
                parent = q.popleft()
                children = isConnected[parent]
                for j, conn in enumerate(children):
                    if j not in visited_set and conn == 1:
                        visited_set.add(j)
                        q.append(j)

        return res
