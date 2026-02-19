from typing import Optional

from leetcode.Neet150.BinaryTree.TreeNode import TreeNode

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(node: Optional[TreeNode]) -> int:

            nonlocal is_balanced

            if not node:
                return 0

            left_height = dfs(node.left) + 1
            right_height = dfs(node.right) + 1

            if left_height - right_height > 1 or right_height - left_height > 1:
                is_balanced = False

            return max(left_height, right_height)

        node = root
        dfs(node)

        return is_balanced
