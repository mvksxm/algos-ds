from typing import List


class Solution:
    def partition_personal(self, s: str) -> List[List[str]]:

        res = []
        def dfs(i: int, list_str: list, partition: list, is_complete: bool):

            """
            Personal version with multi parameter dfs() function.
            n = len(s)
            TC -> O(n*2^n)
            SC -> O(n) + O(n) + O(n) = O(n)
            """

            if is_complete and i >= len(s):
                res.append(partition.copy())
                return

            if i >= len(s): return

            list_str.append(s[i])
            substring = "".join(list_str)

            is_added = False
            if substring == substring[::-1]:
                partition.append(substring)
                is_added = True

            if is_added:
                dfs(i+1, [], partition, is_added)
                partition.pop()

            if i + 1 < len(s):
                dfs(i+1,list_str, partition, is_added)

            list_str.pop()

        dfs(0,[],[], False)
        return res

    def partition(self, s: str) -> List[List[str]]:
        """
        Canonical backtracking version with for loop and indexes.
        n = len(s)
        TC -> O(n*2^n)
        SC -> O(n) (recursion stack)
        """
        res = []
        partition = []

        def dfs(i: int):

            if i >= len(s):
                res.append(partition.copy())
                return

            for j in range(i+1, len(s) + 1):

                substr = s[i:j]
                if substr == substr[::-1]:
                    partition.append(substr)
                    dfs(j)
                    partition.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    sln = Solution()
    print(sln.partition("aab"))