from typing import Optional

from data_structures.TreeNode import TreeNode

# n - amount of nodes
# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach
# Use DFS. Use two limits: lower limit (l_limit) and upper limit (u_limit), both of those vars describe the min / max
# boundaries that can't be crossed, because node will not be considered valid then. The main idea: for the left child
# curr node's val is the upper limit for the right child curr node's val is the lower limit. On each recursive iteration
# limits should be adjusted accordingly according to the val of the node currently inspected, i.e for the left child -
# u_limit = node.val and for right child l_limit = node.val.

# Base case: in case if node is None - return True. It means that were able to iterate until the end and didn't locate
# any invalid nodes

# Validity detection - in case, if curr node's val is l_limit < val < u_limit - it is considered valid. Otherwise - no.
# In case, if it's invalid, we should return False right away, because tree is considered invalid.


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = self.dfs(root, -1001, 1001)
        return is_valid

    def dfs(self, node: TreeNode, l_limit: int, u_limit: int) -> bool:

        if not node:
            return True

        curr_valid = False
        if l_limit < node.val < u_limit:
            curr_valid = True
        else:
            return curr_valid

        left_valid = self.dfs(node.left, l_limit, node.val)
        right_valid = self.dfs(node.right, node.val, u_limit)

        return all([curr_valid, left_valid, right_valid])

