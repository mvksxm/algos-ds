
class DisjointSet:
    def __init__(self, n):
        self._dsu_array = list(range(n))
        self._ranks = [1] * n

    def find(self, i):

        if i >= len(self._dsu_array):
            return None

        if self._dsu_array[i] == i:
            return i

        parent = self.find(self._dsu_array[i])

        # Make sure that parent path updates.
        if parent != self._dsu_array[i]:
            self._dsu_array[i] = parent

        return parent

    def unite(self, i, j):
        if i >= len(self._dsu_array) or j >= len(self._dsu_array):
            raise Exception(f"Index should be in the range between 0 and {len(self._dsu_array)}")

        i_parent = self.find(i)
        j_parent = self.find(j)


        # Added ranking
        i_parent_rank = self._ranks[i_parent]
        j_parent_rank = self._ranks[j_parent]

        if i_parent_rank > j_parent_rank:
            i_parent_rank += j_parent_rank
            self._ranks[i_parent] = i_parent_rank
            self._dsu_array[j_parent] = i_parent
        else:
            j_parent_rank += i_parent_rank
            self._ranks[j_parent] = j_parent_rank
            self._dsu_array[i_parent] = j_parent

