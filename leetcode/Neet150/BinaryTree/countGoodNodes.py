from data_structures.TreeNode import TreeNode
from collections import deque


# Time Complexity: O(n)
# Space Complexity (DFS): O(h); h = height of a recursive call stack
# Space Complexity (BFS): O(w); w = max width of a Binary Tree

# Approach (DFS)
# Initiate the recursive iteration through the tree. Create the 'curr_max' variable that will contain the max value of
# all the parent nodes of a current node that is being inspected currently. In case, if val of a current node is bigger than or equal to
# the 'curr_max' -> update 'curr_max' to the val of a current node, update the cnt_local var from 0 to 1 (it means that
# the current node is a valid one and should be included, when recursion stack will start returning values) and finally
# feed the updated curr_max to deeper recursive calls.
# Base Case: return count = 0

# Approach (BFS)
# Maintain a queue, which would contain a set of nodes at a particular level of a tree. Create a while loop that would
# execute while queue has nodes. Create a cnt var that would c contain the amount of nodes that are valid. Default: 1,
# because, according to constraints, it's guaranteed that there will be one node always present in the input.
# On each iteration of a while loop - pop the node from the queue -> compare its val with the children's vals, in case
# if children's is bigger -> increment cnt var, otherwise do not increment. After comparison update children with the
# max val between their val and parent's val and add them in a queue. Proceed with such an operation until there will
# be no more elements left in a queue.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # res = self.dfs(root, -101)
        res = self.bfs(root)
        return res

    def bfs(self, node) -> int:
        q = deque([node])

        cnt = 1
        while q:
            q_elem = q.popleft()
            l_elem = q_elem.left
            r_elem = q_elem.right

            if l_elem and l_elem.val >= q_elem.val:
                cnt += 1

            if r_elem and r_elem.val >= q_elem.val:
                cnt += 1

            if r_elem:
                r_elem.val = max(r_elem.val, q_elem.val)
                q.append(r_elem)

            if l_elem:
                l_elem.val = max(l_elem.val, q_elem.val)
                q.append(l_elem)

        return cnt


    def dfs(self, node, curr_max) -> int:

        cnt_local = 0
        if not node:
            return 0

        if curr_max <= node.val:
            curr_max = node.val
            cnt_local = 1

        cnt_left = self.dfs(node.left, curr_max)
        cnt_right = self.dfs(node.right, curr_max)

        return cnt_left + cnt_right + cnt_local
