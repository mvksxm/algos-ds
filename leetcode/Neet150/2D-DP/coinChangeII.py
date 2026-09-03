from typing import List


# n -> len(coins)
# m -> amount

# TC -> O(n * m)
# SC -> O(m)

# Approach
# Create an array dp of len amount + 1, which would contain under each i the amount of possibilities to reach the number -> i.
# For amount = 0 (i = 0), we should put 1, because, in case if we reach 0 during our iteration it means that there is an additional 1
# unique possibility exists to reach a specific amount. Initiate for loop and execute the following DP formula ->
# -> dp[i] = dp[i - coin] + dp[i]. After for loop -> return dp[amount]

class Solution:

    # Array DP Approach
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, len(dp)):
                if i >= coin:
                    dp[i] = dp[i - coin] + dp[i]

        return dp[amount]


if __name__ == "__main__":
    sln = Solution()
    print(sln.change(10, [1, 2, 5]))