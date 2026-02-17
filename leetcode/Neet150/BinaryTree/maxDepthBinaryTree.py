from typing import Optional
from TreeNode import TreeNode

# Time Complexity: O(n)
# Space Complexity: O(n) (because of the recursive call stack)

# Approach
# Recursively perform the DFS. Once the base case is hit with the node equal to None - return 0, as the node does not
# exist. At the same time, at the root node add 1 to the 0, because, we know that the root node exists for sure and
# the count should be incremented, in order to reflect that. Perform the same recursive operation for the right node.
# After recursive operation returns - get a max between left count and right count (it's possible that one side has
# more nodes than the other one).

class Solution:
    def maxDepth(self, root: TreeNode) -> Optional[int]:
        if root is None: return 0
        node = root
        return self.countDepth(node)

    def countDepth(self, node: TreeNode) -> int:

        if node is None:
            return 0

        left_count = self.countDepth(node.left) + 1
        right_count = self.countDepth(node.right) + 1

        return max(left_count, right_count)




