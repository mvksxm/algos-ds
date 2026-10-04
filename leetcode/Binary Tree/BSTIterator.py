
# H -> height of Binary Tree
# TC -> hasNext() -> O(1); next() -> average O(1); initialization -> O(H)
# SC -> O(H)

# Approach
# Perform an iterative inorder traversal with stack. In stack maintain prev root nodes of the left subtree. When curr
# node does not have any children anymore -> pop parent from the stack, point pointer to it and then on the next next()
# call explore the right subtree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.roots = []
        self.pointer = self.left_subtree(root, self.roots)


    def left_subtree(self, node, roots):

        while node:
            roots.append(node)
            node = node.left

        return TreeNode()


    def next(self) -> int:

        if not self.pointer: return -1

        if self.pointer.right:
            self.left_subtree(self.pointer.right, self.roots)
            self.pointer = self.roots.pop()
            return self.pointer.val

        if self.roots:
            self.pointer = self.roots[-1]
            self.roots.pop()
            return self.pointer.val

        return -1


    def hasNext(self) -> bool:

        if (
                self.pointer.right
                or self.roots
        ):
            return True

        return False
