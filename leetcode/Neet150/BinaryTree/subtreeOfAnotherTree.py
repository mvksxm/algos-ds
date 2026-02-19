from typing import Optional

from leetcode.Neet150.BinaryTree.TreeNode import TreeNode

# Time Complexity: O(m*n), where m is len of the subTree and n is the the len of a main tree
# Space Complexity: O(m+n)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True
        if not root: return False

        if self. checkIfEqual(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkIfEqual(self, node, subNode):

        if not node and not subNode:
            return True

        if node and subNode and node.val == subNode.val:
            return self.checkIfEqual(node.left, subNode.left) and self.checkIfEqual(node.right, subNode.right)

        return False


