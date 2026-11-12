
# N -> number of nodes in a binary tree
# TC -> O(N)
# SC -> O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = None

        def dfs(node):

            if not node:
                return False

            nonlocal res
            curr = (node == p or node == q)
            left_found = dfs(node.left)
            right_found = dfs(node.right)

            if (curr and left_found) or (curr and right_found) or (left_found and right_found):
                res = node

            return curr or left_found or right_found

        dfs(root)

        return res