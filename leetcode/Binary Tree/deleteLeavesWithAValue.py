
# n -> amount of nodes in a tree
# h -> height of a binary tree

# TC -> O(n)
# SC -> O(h)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        if not root:
            return None

        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)

        if not left and not right and root.val == target:
            return None

        root.left = left
        root.right = right
        return root