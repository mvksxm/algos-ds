from collections import deque

# TC -> O(n)
# SC -> O(n)

# Approach:
# Topological Sort for searching a root; BFS for making sure that the tree is connected.


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:

        freq_l = [0] * n
        graph = {}

        for i in range(n):

            if i not in graph: graph[i] = [-1, -1]

            if leftChild[i] != -1:
                if freq_l[leftChild[i]] >= 1: return False
                graph[i][0] = leftChild[i]
                freq_l[leftChild[i]] += 1

            if rightChild[i] != -1:
                if freq_l[rightChild[i]] >= 1: return False
                graph[i][1] = rightChild[i]
                freq_l[rightChild[i]] += 1

        # Searching for a root
        parent_i = -1
        for i in range(len(freq_l)):
            if freq_l[i] == 0 and parent_i != -1:
                return False

            if freq_l[i] == 0:
                parent_i = i

        if parent_i == -1:  return False

        queue = deque([parent_i])
        visited_set = {parent_i}

        while queue:
            parent = queue.popleft()
            left_child, right_child = graph[parent]

            if left_child not in visited_set and left_child != -1:
                visited_set.add(left_child)
                queue.append(left_child)

            if right_child not in visited_set and right_child != -1:
                visited_set.add(right_child)
                queue.append(right_child)

        return len(visited_set) == n