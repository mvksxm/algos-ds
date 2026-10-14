from collections import deque
from typing import List

# Q -> queries; V -> vertices (unique variables); E -> edges (equations)
# TC -> O(Q * (V+E))
# SC -> O(V+E)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        res = []
        adjacency_list = {}

        for i, (var1, var2) in enumerate(equations):
            if var1 not in adjacency_list: adjacency_list[var1] = []
            if var2 not in adjacency_list: adjacency_list[var2] = []

            adjacency_list[var1].append((var2, values[i]))
            adjacency_list[var2].append((var1,1 / values[i]))

        for start, finish in queries:

            if start not in adjacency_list or finish not in adjacency_list:
                res.append(-1)
                continue

            if start == finish:
                res.append(1)
                continue

            visited_set = {start}
            q = deque([(start, 1)])
            found = False

            while q:
                var, prod = q.popleft()
                for child, mult in adjacency_list[var]:

                    if child == finish:
                        found = True
                        res.append(prod * mult)
                        break

                    if child not in visited_set:
                        visited_set.add(child)
                        q.append((child, prod * mult))

                if found: break

            if not found: res.append(-1)

        return res

if __name__ == "__main__":
    sln = Solution()
    sln.calcEquation([["a","b"],["b","c"],["a","c"]], [2.0,3.0,6.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])