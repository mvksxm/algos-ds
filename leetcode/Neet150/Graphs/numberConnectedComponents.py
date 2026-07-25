from collections import defaultdict
from typing import List

# TC -> O(V+E)
# SC -> O(V+E)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        res = 0

        # Setting up an adjacency list
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited_set = set()
        def dfs(node: int, parent: int | None):
            visited_set.add(node)
            for child in graph[node]:
                if child != parent and child not in visited_set:
                    dfs(child, node)

        for vertex in range(n):
            if vertex in visited_set: continue
            dfs(vertex, None)
            res += 1

        return res

if __name__ == "__main__":
    sln = Solution()

    n = 4
    edges = [[2,3],[1,2],[1,3]]
    print(sln.countComponents(n, edges))