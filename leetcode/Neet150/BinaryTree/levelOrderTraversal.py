from typing import Optional, List

from data_structures.BinaryTree import BinaryTree
from leetcode.Neet150.BinaryTree.TreeNode import TreeNode
from collections import deque


# Time Complexity: O(n)
# Space Complexity (Canonical): O(W), where W = width of a Binary Tree
# Space Complexity (Recursive): O(W+h), where W = max width of a Binary Tree, h - height of the call stack.


# Approach #1 (Canonical BFS)
# Use a queue. When traversing through each parent node at a particular level of a tree -> add each child to the queue
# and at the same time - pop the parent and append it to the local_res array that represents a level that will be added
# to the final array - 'res'. On each iteration of the while loop it's important to get the current length of a queue,
# because it represents the amount of nodes that are supposed to be located in the next level of a Binary Tree.

# Approach #2 (Recursive BFS)
# Use a recursion. Create an array 'res' that will be mutated by the internal operations of the 'dfs' method. On each
# recursive iteration - iterate through currently inspected nodes -> add their values to the 'local_res' arr that will
# be afterward appended to the 'res' array -> get the children of the currently inspected nodes -> add them to a new array
# -> perform a recursive call on them. In the end, return 'res' array.
# Base Case -> children array is empty.


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque([root])

        res = []
        local_res = []
        while q:
            queue_l = len(q)
            for i in range(queue_l):
                queue_elem = q.popleft()
                local_res.append(queue_elem.val)

                if queue_elem.left:
                    q.append(queue_elem.left)
                if queue_elem.right:
                    q.append(queue_elem.right)

            if local_res:
                res.append(local_res)
                local_res = []

        return res



    def levelOrderRecursive(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []

        res = []
        self.bfs([root], res)
        return res

    def bfs(self, nodes_list: list, res: list):

        if not nodes_list:
            return

        child_list = []
        res_row = []
        for node in nodes_list:
            res_row.append(node.val)
            if node.left:
                child_list.append(node.left)
            if node.right:
                child_list.append(node.right)

        res.append(res_row)
        self.bfs(child_list, res)

if __name__ == "__main__":
    tree = BinaryTree([1,2,3,4,5,6,7])
    sln = Solution()
    sln.levelOrder(tree.root())

