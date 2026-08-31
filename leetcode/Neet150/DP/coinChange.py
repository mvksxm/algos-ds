from typing import List

# Approach: Dynamic Programming. Create an array dp, where each idx represents the partial amount of target amount.
# On each cycle of the iteration through the dp array -> check the min amount of coins needed to get the current partial amount
# by iterating through each coin, subtracting that coin from the current partial amount -> (amt - coin). Checking
# min amount of coins, which are needed to get the prev amount dp[amt-coin]. To this prev min amount we are adding 1
# (it represents the current coin) and then we are updating current amount's min by executing the following function ->
# min(dp[amt-coin] + 1, dp[amt]).

# TC -> O(n)
# SC -> O(n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(1, len(dp)):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt - coin] + 1, dp[amt])

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]


if __name__ == "__main__":
    sln = Solution()
    coins = [2, 3]
    amount = 7
    print(sln.coinChange(coins, amount))
