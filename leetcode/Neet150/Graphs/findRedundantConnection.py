from typing import List


# Approach: used DSU data structure to associate nodes with their parents and children with grandparents.

# N -> amount of edges
# TC -> O(N^2)
# SC -> O(N)

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.ranks = [1] * (n + 1)

    def find(self, i):

        if self.parents[i] == i:
            return i

        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def unite(self, i, j) -> bool:
        i_parent = self.find(i)
        j_parent = self.find(j)

        if i_parent == j_parent:
            return False

        i_rank = self.ranks[i_parent]
        j_rank = self.ranks[j_parent]

        if j_rank > i_rank:
            self.parents[i_parent] = j_parent
            self.ranks[j_parent] += 1
        else:
            self.parents[j_parent] = i_parent
            self.ranks[i_parent] += 1

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = DSU(len(edges))

        for edge in edges:
            status = dsu.unite(edge[0], edge[1])
            if not status: return edge

        return []

if __name__ == "__main__":
    sln = Solution()
    edges1=[[1,2],[1,3],[3,4],[2,4]]
    edges2=[[1,4],[3,4],[1,3],[1,2],[4,5]]
    print(sln.findRedundantConnection(edges1))
    print(sln.findRedundantConnection(edges2))