from typing import Optional
from TreeNode import TreeNode

# Time Complexity: O(n)
# Space Complexity: O(n), because of the recursive call stack

# Approach:
# Implement a recursive algorithm. On each recursive iteration call node.right = recursive_call(node.left) and
# node.left = recursive_call(node.right). Make sure that the node.right initially is stored in a separate variable,
# because it will be overwritten by the next recursive call. Base case is supposed to return, when node doesn't have
# a left and a right child.

class Solution:
    def invertTree(self, root: TreeNode) -> Optional[TreeNode]:
        if root is None: return None
        node = root

        if node.left is None and node.right is None:
            return node

        right_node = node.right
        node.right = self.invertTree(node.left)
        node.left = self.invertTree(right_node)

        return node

