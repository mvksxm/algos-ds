
# Approach: Dynamic Programming.
# TC -> O(n)
# SC -> O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        alphabet_ids = set([str(i) for i in range(1, 27)])

        for i in range(len(s)-1, -1, -1):

            if s[i] in alphabet_ids:
                dp[i] = dp[i + 1]

            if i+2 < len(dp) and s[i:i+2] in alphabet_ids:
                dp[i] += dp[i + 2]

            if i < len(s) - 1 and ((i == 0 and s[i] == "0") or (s[i] == "0" and s[i + 1] == "0")):
                return 0


        return dp[0]