
# c -> amount of combinations generated
# k -> length of a single combination
# TC -> O(c * k)
# SC -> O(k) (excluding the output array)

# Approach:
# Backtracking

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        comb = []

        def dfs(start, curr_cnt):

            if curr_cnt == k:
                res.append(comb[:])
                return

            for i in range(start, n + 1):
                comb.append(i)
                dfs(i + 1,curr_cnt + 1)
                comb.pop()

        dfs(1, 0)
        return res


if __name__ == "__main__":
    sln = Solution()
    sln.combine(4, 2)