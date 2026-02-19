from typing import Optional, List
from data_structures.TreeNode import TreeNode


# Time Complexity: O(n)
# Space Complexity: O(h+h), h = height of the tree

# Approach (DFS)
# Perform the DFS. Define an array - res_arr that would store the result and a variable - 'level' that would store
# a currently inspected level of a tree. Start recursive iteration by checking the right subbranch of a tree.
# It's important because, right subbranch is the first one being viewed from the right side. On each iteration -
# check if current level is bigger than the amount of elements in the array -> in case, if it is -> add the val of a
# node to array. Otherwise, ignore the node, because it's 'not visible'.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res_arr = []
        self.dfs(root, res_arr, 1)
        return res_arr

    def dfs(self, node, arr, level):
        if not node:
            return

        if level > len(arr):
            arr.append(node.val)

        self.dfs(node.right, arr, level + 1)
        self.dfs(node.left, arr, level + 1)