from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach: perform a bottom-up dfs. Once reached the end -> start calculating sums. On each recursion return ->
# calculate curr global max by adding node.val + left_sm (if positive) + right_sm (if positive) and update it if it's
# bigger than the curr global max returned from the bottom left call and right bottom call.
# In addition to returning a global_max, return the curr biggest_path by calculating the max(node.val, node.val + left_sm,
# node.val + right_sm).

# TC -> O(n); n - amount of nodes in a tree
# SC -> O(H); H - height of the recursion stack

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, float('-inf')

            local_sm = node.val
            left_sm, g_sm_left = dfs(node.left)
            right_sm, g_sm_right = dfs(node.right)

            if left_sm > 0: local_sm += left_sm
            if right_sm > 0: local_sm += right_sm

            biggest_path = max(node.val, node.val + left_sm, node.val + right_sm)

            return biggest_path, max(g_sm_left, g_sm_right, local_sm)

        _, g_sm = dfs(root)

        return g_sm