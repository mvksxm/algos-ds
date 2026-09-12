
# DP with memoization
# m = len(s); n = len(t)
# TC -> O(m * n)
# SC -> O(m * n)


class Solution:

    # DP with memoization
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(t_i, s_i):

            state = (t_i, s_i)
            if state in dp:
                return dp[state]

            if t_i >= len(t):
                return 1

            if s_i >= len(s):
                return 0

            if t[t_i] == s[s_i]:
                count = dfs(t_i + 1, s_i + 1) + dfs(t_i, s_i + 1)
            else:
                count = dfs(t_i, s_i + 1)

            dp[state] = count
            return count

        return dfs(0, 0)

if __name__ == "__main__":
    sln = Solution()
    s = "rabbbitrabbit"
    t = "rabbit"
    print(sln.numDistinct(s, t))

#   c a a a t
# c     0 0 0
# a     1 1 0
# t     0 0 1
