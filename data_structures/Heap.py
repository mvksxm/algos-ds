# Test Examples:
#      0
#    /  \
#   2    1
#  / \   /
# 6   4  5

#     0
#    /  \
#   1    6
#  / \
# 4   5

#     0
#    /  \
#   1     3
#  / \   / \
# 2   4  7  5

#      5 -> 0
#    /   \
#   6     1  -> 0; 5
#  / \    /
# 2   4  0 -> 1
# [5, 6, 1, 2, 4, 0]

#     4
#    / \
#   2   3
#  / \
# 1   6

#     7
#   /   \
#  6     3
# / \    /
#4   5  2


class BaseHeap:
    def __init__(self, values):
        self.values = values

    def _left_child_idx(self, parent_idx) -> int:
        return (parent_idx * 2) + 1

    def _right_child_idx(self, parent_idx) -> int:
        return (parent_idx * 2) + 2

    def _parent_idx(self, child_idx) -> int:
        return (child_idx - 1) // 2

    def _get_left_child(self, parent_idx: int) -> [int, None]:
        l_index = self._left_child_idx(parent_idx)

        if l_index > len(self.values) - 1:
            return None

        return self.values[l_index]

    def _get_right_child(self, parent_idx: int) -> [int, None]:
        r_index = self._right_child_idx(parent_idx)

        if r_index > len(self.values) - 1:
            return None

        return self.values[r_index]

    def _get_parent(self, child_idx: int) -> int:
        return self.values[self._parent_idx(child_idx)]

    def _build_heap(self):
        raise NotImplemented("'_build_heap()' method should be implemented!")

    def _heapify(self, idx: int):
        raise NotImplemented("'_heapify()' method should be implemented!")

    def get_values(self):
        return self.values

    def add(self, val: int):
        raise NotImplemented("'add()' method should be implemented!")

    def remove(self, idx: int):
        raise NotImplemented("'remove()' method should be implemented!")

    def get(self):
        raise NotImplemented("'pop()' method should be implemented!")


class MinHeap(BaseHeap):
    def __init__(self, values: list):

        self._values = values
        super().__init__(self._values)

        if self._values:
            self._build_heap()# My Implementation

    def _build_heap(self):

        """
        _build_heap() method
        Purpose - Iterates through the non-leaf nodes of a Heap Tree and 'heapifying' their children.
        Complexity - O(N); N - number of nodes in a Heap.
        """

        last_parent_idx = (len(self._values) - 1) // 2

        for i in range(last_parent_idx, -1, -1):
            self._heapify(i)

    def _heapify(self, idx: int):

        """
        _heapify() method
        Purpose - Orders a subbranch of a Heap Tree according to rules of the data structure.
        Complexity - O(N); N - number of nodes in the Heap's subbranch
        """

        if idx > len(self._values) - 1:
            return

        parent = self._values[idx]
        l_child = self._get_left_child(idx)
        r_child = self._get_right_child(idx)

        min_idx = idx
        if l_child is not None and l_child < parent:
            min_idx = self._left_child_idx(idx)

        if r_child is not None and (r_child < parent and r_child < l_child):
            min_idx = self._right_child_idx(idx)

        if min_idx != idx:
            curr_val = self._values[idx]
            min_val = self._values[min_idx]

            self._values[min_idx] = curr_val
            self._values[idx] = min_val

            self._heapify(min_idx) # min_idx is the index of a bigger value that was swapped with the minimum one.

    def _propagate_upwards(self, idx):

        """
        _propagate_upwards() method
        Purpose - Propagates the value (in case, if it's smaller than its parent) up the Heap data structure.
        Complexity - O(log N); N - number of nodes in a Heap
        """

        parent_idx = self._parent_idx(idx)
        val = self._values[idx]
        parent = self._get_parent(idx)

        while parent_idx >= 0 and self._values[idx] < parent:

            self._values[idx] = parent
            self._values[parent_idx] = val

            idx = parent_idx
            parent_idx = self._parent_idx(idx)
            parent = self._get_parent(idx)

    def add(self, val: int):
        """
        add() method
        Purpose - Adds a new value in the Heap data structure
        Complexity - O(log N); N - number of nodes in a Heap
        """

        self._values.append(val)
        val_idx = len(self._values) - 1
        self._propagate_upwards(val_idx)

    def remove(self, idx: int):

        """
        remove() method
        Purpose - Removes a value under specific index from the Heap data structure
        Complexity - O(log N) + O(log N); N - number of nodes in a Heap
        """

        if idx > len(self._values) - 1:
            return

        self._values[idx] = -float('inf')
        self._propagate_upwards(idx)
        self._values[0] = self._values.pop()
        self._heapify(0)

    def get(self):

        """
        get() method
        Purpose - Gets the top value from the Heap
        Complexity - O(log N); N - number of nodes in a Heap
        """

        if not self._values:
            return None

        if len(self._values) == 1:
            return self._values.pop()

        res = self._values[0]
        self._values[0] = self._values.pop()
        self._heapify(0)

        return res

class MaxHeap(BaseHeap):
    def __init__(self, values: list):

        self._values = values
        super().__init__(self._values)

        if self._values:
            self._build_heap()

    def _build_heap(self):

        """
        _build_heap() method
        Purpose - Iterates through the non-leaf nodes of a Heap Tree and 'heapifying' their children.
        Complexity - O(N); N - number of nodes in a Heap.
        """

        last_parent_idx = (len(self._values) - 1) // 2

        for i in range(last_parent_idx, -1, -1):
            self._heapify(i)

    def _heapify(self, idx: int):

        """
        _heapify() method
        Purpose - Orders a subbranch of a Heap Tree according to rules of the data structure.
        Complexity - O(N); N - number of nodes in the Heap's subbranch
        """

        if idx > len(self._values) - 1:
            return

        parent = self._values[idx]
        l_child = self._get_left_child(idx)
        r_child = self._get_right_child(idx)

        max_idx = idx
        if l_child is not None and l_child > parent:
            max_idx = self._left_child_idx(idx)

        if r_child is not None and (r_child > parent and r_child > l_child):
            max_idx = self._right_child_idx(idx)

        if max_idx != idx:
            curr_val = self._values[idx]
            max_val = self._values[max_idx]

            self._values[max_idx] = curr_val
            self._values[idx] = max_val

            self._heapify(max_idx) # min_idx is the index of a bigger value that was swapped with the minimum one.

    def _propagate_upwards(self, idx):

        """
        _propagate_upwards() method
        Purpose - Propagates the value (in case, if it's bigger than its parent) up the Heap data structure.
        Complexity - O(log N); N - number of nodes in a Heap
        """

        parent_idx = self._parent_idx(idx)
        val = self._values[idx]
        parent = self._get_parent(idx)

        while parent_idx >= 0 and self._values[idx] > parent:

            self._values[idx] = parent
            self._values[parent_idx] = val

            idx = parent_idx
            parent_idx = self._parent_idx(idx)
            parent = self._get_parent(idx)

    def add(self, val: int):

        """
        add() method
        Purpose - Adds a new value in the Heap data structure
        Complexity - O(log N); N - number of nodes in a Heap
        """

        self._values.append(val)
        val_idx = len(self._values) - 1
        self._propagate_upwards(val_idx)

    def remove(self, idx: int):

        """
        remove() method
        Purpose - Removes a value under specific index from the Heap data structure
        Complexity - O(log N) + O(log N); N - number of nodes in a Heap
        """

        if idx > len(self._values) - 1:
            return

        self._values[idx] = float('inf')
        self._propagate_upwards(idx)
        self._values[0] = self._values.pop()
        self._heapify(0)

    def get(self):

        """
        get() method
        Purpose - Gets the top value from the Heap
        Complexity - O(log N); N - number of nodes in a Heap
        """

        if len(self._values) == 0:
            return None

        if len(self._values) == 1:
            return self._values.pop()

        res = self._values[0]
        self._values[0] = self._values.pop()
        self._heapify(0)

        return res



if __name__ == "__main__":
    arr = [5, 6, 1, 2, 4, 7, 3]
    min_heap = MinHeap(arr)
    print(min_heap.get_values())
    print(min_heap.get())
    print(min_heap.get_values())

    max_heap = MaxHeap(arr)
    print(max_heap.get_values())
    print(max_heap.get())
    print(max_heap.get_values())

