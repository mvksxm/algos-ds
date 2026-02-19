from typing import Optional

import graphviz

from TreeNode import TreeNode

class BinaryTree:
    def __init__(self, arr):
        self._arr = arr
        self._root_node = self._generate_binary_tree()

    def root(self) -> TreeNode:
        return self._root_node

    def _generate_binary_tree(self) -> Optional[TreeNode]:
        root = self._recursive_balanced_tree_generator(0)
        return root

    def _recursive_balanced_tree_generator(self, node_idx) -> Optional[TreeNode]:

        if node_idx >= len(self._arr):
            return None

        node_val = self._arr[node_idx]
        if node_val is None:
            return None

        node = TreeNode(val = node_val)
        
        left_child_idx = node_idx * 2 + 1
        right_child_idx = node_idx * 2 + 2

        node.left = self._recursive_balanced_tree_generator(left_child_idx)
        node.right = self._recursive_balanced_tree_generator(right_child_idx)

        return node

    def display_binary_tree(self):
        g = graphviz.Digraph('Binary Tree')
        dedup_map = {}

        def recursively_display(node: TreeNode):

            if node is None:
                return None

            node_val = str(node.val)
            node_id: str

            if node_val in dedup_map:
                suffix = dedup_map[node_val] + 1
                dedup_map[node_val] = suffix
                node_id = f"{node_val}-{suffix}"
            else:
                dedup_map[node_val] = 1
                node_id = node_val + "-1"

            g.node(node_id, label=node_val)
            left_id = recursively_display(node.left)
            right_id = recursively_display(node.right)

            if left_id is not None:
                g.edge(node_id, left_id)

            if right_id is not None:
                g.edge(node_id, right_id)

            return node_id

        recursively_display(self._root_node)
        g.view()