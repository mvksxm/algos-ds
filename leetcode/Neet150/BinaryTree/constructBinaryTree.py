from collections import defaultdict
from typing import List, Optional

# Approach: divide and conquer. By using the preorder array - identify the current level's root and by using inorder
# array - identify nodes from the left subtree and from the right subtree. Then perform this operation repeatedly on
# left children and right children until there will be node that does not have any children (base case).

# TC -> O(n)
# SC -> O(n) + O(log n) = O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = defaultdict(int)
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def dfs(left_pre, right_pre, left_in):

            if left_pre == right_pre:
                return None

            parent = preorder[left_pre]
            parent_node = TreeNode(preorder[left_pre])
            parent_idx = inorder_map[parent]
            left_tree_len = parent_idx - left_in

            left_child = dfs(left_pre + 1, left_pre + 1 + left_tree_len, left_in)
            right_child = dfs(left_pre + 1 + left_tree_len, right_pre, parent_idx + 1)

            parent_node.left = left_child
            parent_node.right = right_child

            return parent_node

        return dfs(0, len(preorder), 0)