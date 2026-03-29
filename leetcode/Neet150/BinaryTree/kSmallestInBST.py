from typing import Optional

from data_structures.TreeNode import TreeNode

# Time Complexity: O(n) or O(k); O(k), in case, if we reach k number - we return immediately, however, it's possible that
# k will be equal to n, so the option that iteration will go through all the nodes is also possible.

# Space Complexity: O(h); where h is the height of the recursion stack.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node: TreeNode, count):

            if count > k:
                return None, count

            if not node:
                return None, count

            if not node.left and not node.right:
                return node.val, count + 1

            left_val, left_count = dfs(node.left, count)

            if left_count == k:
                return left_val, left_count

            if left_count + 1 == k:
                return node.val, left_count + 1

            right_val, right_count = dfs(node.right, left_count + 1)


            if not right_val:
                return node.val, left_count + 1

            return right_val, right_count


        node_val, _ = dfs(root, 0)
        return node_val



