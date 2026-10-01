# N - nodes in a graph; E - edges in a graph
# TC -> O(E · α(N))
# SC -> O(N)
# Approach: DSU

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n


    def find(self, i):

        if self.parents[i] == i: return i

        parent = self.find(self.parents[i])

        # path compression
        if self.parents[i] != parent:
            self.parents[i] = parent

        return parent

    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)

        i_rank = self.ranks[i_parent]
        j_rank = self.ranks[j_parent]

        if i_rank > j_rank:
            self.ranks[i_parent] += j_rank
            self.parents[j_parent] = i_parent
        else:
            self.ranks[j_parent] += i_rank
            self.parents[i_parent] = j_parent


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        connected_nodes = len({node for edge in connections for node in edge})
        dsu = DSU(n)
        can_detach = 0

        parents = set()

        for conn in connections:
            first, second = conn
            first_parent = dsu.find(first)
            second_parent = dsu.find(second)

            if first_parent != second_parent:
                parents.discard(first_parent)
                parents.discard(second_parent)
                parents.add(dsu.union(first, second))
            else:
                can_detach += 1

        to_attach = (len(parents) - 1) + (n - connected_nodes)
        can_detach = can_detach - to_attach

        return to_attach if can_detach >= 0 else -1

if __name__ == "__main__":
    sln = Solution()
    sln.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]])
