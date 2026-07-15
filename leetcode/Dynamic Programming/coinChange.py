import collections
from typing import List

from tester import Tester


# DP Solutions
# Amount - A; Coins Array Len - C
# TC -> O(A*C); Explanation: A as the amount of unique states, which are computed only once and multiplied by len of coins array,
# because for each unique state we are considering a possibility to use each one of the available coins.
# SC -> O(A)


class Solution:

    # dp top-down approach
    def coinChangeDp(self, coins: List[int], amount: int) -> int:

        if not amount: return 0

        reversed_coins = sorted(coins, reverse=True)
        dp = {}

        def dfs(number: int):

            if number < 0:
                return float('inf')

            if number == 0:
                dp[number] = 0
                return 0

            if number in dp: return dp[number]

            curr_min = float('inf')
            for coin in reversed_coins:
                curr_min = min(curr_min, dfs(number - coin))

            if curr_min == float('inf'):
                dp[number] = curr_min
                return curr_min

            dp[number] = curr_min + 1
            return curr_min + 1

        coins_amount = dfs(amount)
        if coins_amount == float('inf'): return -1
        return coins_amount

    # dp bottom up approach
    def coinChangeBottomUp(self, coins: List[int], amount: int) -> int:

        if not amount: return 0

        dp = [10**4 + 1] * (amount + 1)
        dp[0] = 0

        for amnt in range(1, len(dp)):

            for coin in coins:
                if coin <= amnt:
                    dp[amnt] = min(dp[amnt], dp[amnt - coin] + 1)


        return dp[-1] if dp[-1] != 10**4 + 1 else -1



if __name__ == "__main__":
    sln = Solution()
    tst = Tester()


    test_list = [
        # Official examples
        [[[1, 2, 5], 11], 3],
        [[[2], 3], -1],
        [[[1], 0], 0],

        # Single coin cases
        [[[1], 1], 1],
        [[[1], 5], 5],
        [[[5], 5], 1],
        [[[5], 3], -1],

        # Simple combinations
        [[[1, 3, 4], 6], 2],
        [[[1, 2, 3], 7], 3],
        [[[2, 5, 10, 1], 27], 4],

        # Impossible cases
        [[[2, 4], 7], -1],
        [[[3, 5], 7], -1],
        [[[5, 10], 1], -1],

        # Target smaller than all coins
        [[[2, 5, 10], 1], -1],
        [[[2, 5, 10], 4], 2],

        # Greedy pitfalls
        [[[1, 3, 4], 6], 2],
        [[[2, 3, 5], 7], 2],
        [[[1, 5, 6, 9], 11], 2],

        # Duplicate coins
        [[[1, 1, 2], 4], 2],
        [[[2, 2, 4], 8], 2],

        # Larger targets
        [[[1, 2, 5], 100], 20],
        [[[1, 2, 5], 999], 201],
        [[[186, 419, 83, 408], 6249], 20],

        # Many coins
        [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50], 5],

        # Empty / edge cases
        [[[], 0], 0],
        [[[], 5], -1],
        [[[0], 0], 0],

        # DP-focused cases
        [[[2, 5, 10, 1], 18], 4],
        [[[9, 6, 5, 1], 11], 2],
        [[[2, 4, 5], 13], 3],

        # Large coin values
        [[[186, 419, 83, 408], 1000], 8],

        # Unique optimal combinations
        [[[2, 7, 10], 14], 2],
        [[[3, 7, 405, 436], 12], 4],
    ]

    tst.array_test(test_list, sln.coinChangeBottomUp)

#     11
#   / | \
#  5  2  1
#  |
#  6
#  |
#  5
#  |
#  1
#  |
#  0