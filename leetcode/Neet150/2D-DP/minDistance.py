
# m -> len(word1)
# n -> len(word2)
# TC -> O(m * n)
# SC -> O(m * n)

# Approach
# DP state - (word1_idx, word2_idx): min_operations
# Operations performed (Increment total operations amount by 1, when doing any of those):
# For removal -> move word1 pointer further, leave pointer of the word2 as it is.
# For update ->  move word1 pointer further, move  pointer of the word2 further as well.
# For adding ->  leave word1 pointer as it is, move  pointer of the word2 further.
# If chars are equal -> increment both pointers and do not increment the total operations amount.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(word1_i, word2_i):
            cache_idx = (word1_i, word2_i)

            if cache_idx in dp:
                return dp[cache_idx]

            if word1_i >= len(word1) and word2_i < len(word2):
                # Final additions
                steps = len(word2) - word2_i
                dp[cache_idx] = steps
                return steps


            if word2_i >= len(word2) and word1_i < len(word1):
                # Final removals
                steps = len(word1) - word1_i
                dp[cache_idx] = steps
                return steps

            # Base Case
            if word1_i >= len(word1):
                return 0

            min_steps = 0
            if word1[word1_i] == word2[word2_i]:
                min_steps = dfs(word1_i + 1, word2_i + 1)
                dp[cache_idx] = min_steps
            else:
                replace_steps = 1 + dfs(word1_i + 1, word2_i + 1)
                delete_steps = 1 + dfs(word1_i + 1, word2_i)
                insert_steps = 1 + dfs(word1_i, word2_i + 1)

                min_steps = min(replace_steps, delete_steps, insert_steps)
                dp[cache_idx] = min_steps

            return min_steps

        return dfs(0, 0)

if __name__ == "__main__":
    sln = Solution()
    print(sln.minDistance("intention", "execution"))