from collections import defaultdict
from typing import List

# Approach - DFS to find all affected methods and then iteration through all the unaffected methods in order to find an
# intersection. If intersection found -> return all methods; otherwise return only unaffected methods in the res_set.

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        # Adjacency list and frequency array
        adjacency_list = defaultdict(list)

        for inv in invocations:
            adjacency_list[inv[0]].append(inv[1])

        res_set = set()
        affected_set = set()
        def dfs_affected(idx):
            if idx in affected_set: return

            affected_set.add(idx)
            for child_m in adjacency_list[idx]:
                dfs_affected(child_m)

        dfs_affected(k)

        intersected = False
        for i in range(n):
            inv = adjacency_list[i]
            not_affected = i not in affected_set
            if not_affected:
                res_set.add(i)

            if not_affected and any([func in affected_set for func in inv]):
                intersected = True

        if intersected: res_set = (res_set | affected_set)

        return [m for m in res_set]

if __name__ == "__main__":
    sln = Solution()
    print(sln.remainingMethods(3,2, [[2,1],[1,0],[0,1]]))