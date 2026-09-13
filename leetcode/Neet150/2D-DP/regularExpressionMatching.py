
# m -> len(s); n -> len(p)
# TC -> O(m * n)
# SC -> O(m * n)

# Approach
# dp state -> (idx_s, idx_p): is possible to match (bool type)


class Solution:

    # DP with memoization
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(idx_s, idx_p):

            key = (idx_s, idx_p)
            if key in dp:
                return dp[key]

            # Base Cases
            if idx_s >= len(s) and idx_p >= len(p):
                return True

            if idx_p >= len(p):
                return False

            is_possible = False

            if idx_p < len(p) - 1 and p[idx_p + 1] == "*":
                is_possible = any([dfs(idx_s, idx_p + 1), dfs(idx_s, idx_p + 2)])
            elif p[idx_p] == "*":
                prev_char = p[idx_p - 1]
                if idx_s >= len(s) or (prev_char != s[idx_s] and prev_char != "."):
                    dp[(idx_s, idx_p)] = False
                    return False
                is_possible = any([dfs(idx_s + 1, idx_p), dfs(idx_s + 1, idx_p + 1)])
            elif idx_s < len(s) and (p[idx_p] == "." or s[idx_s] == p[idx_p]):
                is_possible = dfs(idx_s + 1, idx_p + 1)

            dp[key] = is_possible
            return is_possible

        return dfs(0, 0)



if __name__ == "__main__":
    sln = Solution()
    print(sln.isMatch("a", ".*..a*"))