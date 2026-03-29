
class DisjointSet:
    def __init__(self, n):
        self._dsu_array = list(range(n))

    def find(self, i):

        if i >= len(self._dsu_array):
            return None

        if self._dsu_array[i] == i:
            return i

        return self.find(self._dsu_array[i])


    def unite(self, i, j):
        if i >= len(self._dsu_array) or j >= len(self._dsu_array):
            raise Exception(f"Index should be in the range between 0 and {len(self._dsu_array)}")

        i_parent = self.find(i)
        j_parent = self.find(j)

        self._dsu_array[j_parent] = i_parent
