from TreeNode import TreeNode

# Time Complexity: O(n)
# Space Complexity: O(n) (len of recursive call stack)


# Approach:
# Create a recursive nested function inside a main function. Maintain a global var - global_max that would contain
# the max sum of the amount of left edges and right edges of a particular node. On each recursive call calculate the
# amount of ledges from the left side and from the right side of a node, sum them and update the global_max if it is smaller.
# Recursive function itself on each call should return the max between amount of edges encountered from the left and
# from the right, in order to get the max amount at a specific level of a tree.

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        global_max = 0

        def count_diameter(node: TreeNode):

            if node is None:
                return 0

            left_diameter = count_diameter(node.left)
            right_diameter = count_diameter(node.right)

            nonlocal global_max
            global_max = max(global_max, left_diameter + right_diameter)

            return max(left_diameter + 1, right_diameter + 1)

        node = root
        count_diameter(node)

        return global_max