# DP with memoization

# n -> len(s1); m -> len(s2)
# TC -> O(n * m)
# SC -> O(n * m)

# Approach
# DP State -> (s1_idx, s2_idx): bool (is it possible from curr s1_idx and s2_idx reach the end of s3).
# If s1[s1_idx] == s2[s2_idx] == s3[s3_idx] -> we need to check both possibilities of picking s1_idx + 1 or s2_idx + 1
# as the next idx. Otherwise, we are picking next character as s1_idx + 1 if s1[s1_idx] == s3[s3_idx] or s2_idx + 1
# if s1[s2_idx] == s3[s3_idx].

class Solution:
    # DP with memoization
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        if len(s1) + len(s2) != len(s3): return False

        def dfs(s1_idx, s2_idx, s3_idx):

            if (s1_idx, s2_idx) in dp:
                return dp[(s1_idx, s2_idx)]

            s1_valid = s1_idx < len(s1)
            s2_valid = s2_idx < len(s2)
            both_valid = s1_valid and s2_valid

            if s1_idx >= len(s1) and s2_idx >= len(s2) and s3_idx >= len(s3):
                return True

            res = False
            if both_valid and s3[s3_idx] == s2[s2_idx] and s3[s3_idx] == s1[s1_idx]:
                res = any([
                    dfs(s1_idx + 1, s2_idx, s3_idx + 1),
                    dfs(s1_idx, s2_idx + 1, s3_idx + 1)
                ])
            elif s1_valid and s3[s3_idx] == s1[s1_idx]:
                res = dfs(s1_idx + 1, s2_idx, s3_idx + 1)
            elif s2_valid and s3[s3_idx] == s2[s2_idx]:
                res = dfs(s1_idx, s2_idx + 1, s3_idx + 1)

            dp[(s1_idx, s2_idx)] = res
            return res


        return dfs(0, 0, 0)

if __name__ == "__main__":
    sln = Solution()
    s1="aaaa"
    s2="bbbb"
    s3="aabbbbaa"
    print(sln.isInterleave(s1, s2, s3))