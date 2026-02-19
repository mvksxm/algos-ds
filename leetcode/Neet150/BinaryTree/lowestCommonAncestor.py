from leetcode.Neet150.BinaryTree.TreeNode import TreeNode


# Time Complexity: O(h); h = height
# Space Complexity: O(h); h = height

# Approach
# Performing recursive DFS. In case, if current node's value is bigger than or equal to p's value and, at the same time, smaller than
# or equal to the value of a q, it means that the lowest possible ancestor was reached for both the p and q, because,
# after that, recursive iteration would go deeper, but in separate tree branches that contain either single p or q at
# most. The same logic works, in case if p's value is >= root.val >= q.val.

# However, in case, if both of the searched nodes are either smaller or bigger than the val under the root.val, then
# recursive iteration should proceed further to either left branch (nodes' values are smaller) or right branch (nodes'
# values are bigger), until there will be a node that would fall under conditions described in the first paragraph.

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val <= root.val <= q.val:
            return root

        if p.val >= root.val >= q.val:
            return root

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return self.lowestCommonAncestor(root.left, p, q)




