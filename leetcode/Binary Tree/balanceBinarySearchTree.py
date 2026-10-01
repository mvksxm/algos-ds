
# n -> amount of nodes in a tree
# TC -> O(n)
# SC -> O(n)
# Approach: Compress the tree to an array by using an inorder traversal. Perform Binary Search on the array where
# curr pivot is root, pivot of the left array is left child and pivot of the right array is a right child.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def to_array(self, node, arr):

        if not node:
            return

        self.to_array(node.left, arr)
        arr.append(node)
        self.to_array(node.right, arr)

    def balance(self, l_p, r_p, arr):

        if l_p > r_p:
            return None

        pivot = l_p + (r_p - l_p) // 2
        mid_node = arr[pivot]

        mid_node.left = self.balance(l_p, pivot - 1, arr)
        mid_node.right = self.balance(pivot + 1, r_p, arr)
        return mid_node


    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:

        if not root: return None

        arr_bst = []
        self.to_array(root, arr_bst)

        return self.balance(0, len(arr_bst) - 1, arr_bst)