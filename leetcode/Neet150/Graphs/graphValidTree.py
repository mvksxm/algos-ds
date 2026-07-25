from collections import defaultdict
from typing import List

# TC -> O(V+E)
# SC -> O(V+E)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges and n == 1: return True
        if len(edges) != n - 1: return False

        # Set up a graph map
        graph = defaultdict(set)

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        visited_set = set()
        def dfs(node: int) -> bool:
            next_nodes = graph[node]
            visited_set.add(node)
            for n_node in next_nodes:
                if n_node in visited_set: return False
                graph[n_node].remove(node)
                if not dfs(n_node): return False

            return True

        if not dfs(edges[0][0]) or len(visited_set) != n:
            return False

        return True