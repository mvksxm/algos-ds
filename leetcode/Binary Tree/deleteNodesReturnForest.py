from typing import Optional, List

from data_structures.TreeNode import TreeNode


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        if not root: return []

        to_delete_set = {val for val in to_delete}
        result = []

        def dfs(node: TreeNode):
            if not node: return None

            left_node = dfs(node.left)
            right_node = dfs(node.right)

            if node.val in to_delete_set:
                if left_node: result.append(left_node)
                if right_node: result.append(right_node)
                return None

            node.left = left_node
            node.right = right_node
            return node

        modified_root = dfs(root)
        if modified_root: result.append(modified_root)
        return result

