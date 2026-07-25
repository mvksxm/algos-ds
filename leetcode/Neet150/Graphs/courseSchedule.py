from collections import defaultdict, deque
from typing import List


# TC -> O(V+E)
# SC -> O(V+E)

# Approach (DFS)
# 1) Create a map that would contain keys in a form of the vertices (nodes) and values in a form of the arrays of edges
# pointing to the child vertices.
# 2) Use DFS to traverse down the course graph, at the same time set-based variable -> 'path' should be maintained in order
# to track nodes that were visited already. In case if visited node is encountered -> return False right away. In case if
# recursion returns successfully and all children were validated -> then all of them should be removed from the
# node's children array, so that, when performing a traverse from the parent node, an additional computation was avoided.

# Approach (BFS) (Kahn's Algorithm)
# 1) Create a map that would contain keys in a form of the vertices (nodes) and values in a form of the arrays of edges
# # pointing to the child vertices.
# 2) Create an array that would contain vertices as indexes and values as the amount of edges pointing to them.
# 3) Perform a BFS. To the BFS queue input vertices that have 0 dependencies (0 edges pointing to them). On each BFS
# iteration, when iterating through the children of a particular node in a queue, decrement the amount of dependencies
# for a child by 1. In case if child has an amount of dependencies < 0 -> return False (it means it was already a part
# of the queue)
# 4) The expected result after the BFS is that all nodes have been visited and have 0 dependencies.If it's
# not the case and dependency_count array contains even a single non-zero value -> return False.
# 5) If all previous checks have been passed -> return True.


class Solution:
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])

        def dfs(root: int, path: set):
            children = graph[root]
            for child in children:

                if child in path: return False
                path.add(child)
                if not dfs(child, path): return False
                path.remove(child)

            graph[root] = []
            return True

        for key in list(graph.keys()):
            if not dfs(key, {key}): return False

        return True

    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        child_map = defaultdict(list)
        dependency_count = [0] * numCourses
        queue = deque()

        for prereq in prerequisites:
            child_map[prereq[1]].append(prereq[0])
            dependency_count[prereq[0]] += 1

        for i in range(len(dependency_count)):
            if dependency_count[i] == 0: queue.append(i)

        if not queue: return False

        while queue:
            left_elem = queue.popleft()
            for child in child_map[left_elem]:
                dependency_count[child] -= 1
                if dependency_count[child] == 0: queue.append(child)
                if dependency_count[child] < 0: return False

        if any(dependency_count): return False
        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.canFinishBFS(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))

        #
        #
        # if not search_set: return False
        # queue = deque([node for node in search_set])
        #
        # while queue:
        #     parent = queue.popleft()
        #
        #
        # pass



# set
# 1 -> 2, 3; 2 -> 3:
#  1
# |  \
# 2 - 3


# First Approach (Not memory optimized).
# set up the map, where parents will be pointing to children
# create a map, with a key equal to child and a value equal to the set of parents.
# run BFS and, on adding children to the queue, check if a child is in the parents set; if it is -> return false;
# return true, if a len(map) + 1 == numCourses (+1, because there will be nodes that have parents, however there is still
# one node that should be the root of the graph.

# Second Approach