from typing import Optional

from leetcode.Neet150.BinaryTree.TreeNode import TreeNode

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False