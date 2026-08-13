from collections import deque
from typing import Optional


# Approach - use BFS to encode and decode. Specifically, on each iteration of the while loop, pop parent from queue then
# place left and right child back to the queue and to the encoding list (left first, right second).

# n - amount of nodes in the Binary Tree
# TC -> O(n)
# SC -> O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def tree_encode(self, node):

        s_array = [str(node.val)]
        queue = deque([node])

        while queue:
            f_item = queue.popleft()
            node_left = f_item.left
            node_right = f_item.right

            if node_left:
                queue.append(node_left)
                s_array.append(str(node_left.val))
            else:
                s_array.append("")

            if node_right:
                queue.append(node_right)
                s_array.append(str(node_right.val))
            else:
                s_array.append("")

        return s_array


    def tree_decode(self, d_array):

        root_node = iter_node = TreeNode(int(d_array[0]))
        queue = deque([(iter_node, 0)])

        while queue:
            last_idx = queue[-1][-1]
            left_idx = last_idx + 1
            right_idx = last_idx + 2

            f_item = queue.popleft()
            q_node = f_item[0]

            if not q_node: continue

            if left_idx < len(d_array):
                left_node = TreeNode(int(d_array[left_idx])) if d_array[left_idx] != "" else None
                q_node.left = left_node
                queue.append((left_node, left_idx))

            if right_idx < len(d_array):
                right_node = TreeNode(int(d_array[right_idx])) if d_array[right_idx] != "" else None
                q_node.right = right_node
                queue.append((right_node, right_idx))


        return root_node

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root: return ""

        s_array = self.tree_encode(root)
        right_boundary = 0
        for i in range(len(s_array)-1, -1, -1):
            if s_array[i] != "":
                right_boundary = i
                break

        print(",".join(s_array[:right_boundary + 1]))
        return ",".join(s_array[:right_boundary + 1])

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        d_array = data.split(",")
        return self.tree_decode(d_array)