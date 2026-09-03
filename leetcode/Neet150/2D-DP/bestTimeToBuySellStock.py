from typing import List


# Brute Force Solution
# TC -> O(n^2)
# SC -> O(n)

# Dynamic Programming Solution
# TC -> O(n)
# SC -> O(n)

# Example
# [1, 5, 2, 4, 3, 6]
# buy =  [7, 4, 4, 3, 3, -6]; mx_buy = 4; dp formula for buying -> max(-buy + sell[i + 1], -buy, mx_buy)
# sell = [5, 8, 6, 6, 6,  6]; mx_sell = 8; dp formula for selling -> max(sell + buy[i + 2], sell, mx_sell)

class Solution:

    # Brute Force
    def maxProfitBrute(self, prices: List[int]) -> int:
        dp = {}
        def dfs(idx, is_bought):

            if (idx, is_bought) in dp:
                return dp[(idx, is_bought)]

            if idx >= len(prices):
                return 0

            if is_bought:
                base_profit = -prices[idx]
            else:
                base_profit = prices[idx]

            local_profit = base_profit

            for i in range(idx + 1, len(prices)):
                if is_bought:
                    profit = base_profit + dfs(i, False)
                    local_profit = max(profit, local_profit)

                if i - idx > 1 and not is_bought:
                    profit = base_profit + dfs(i, True)
                    local_profit = max(profit, local_profit)

            dp[(idx, is_bought)] = local_profit
            return local_profit

        max_profit = 0
        for j in range(len(prices)):
            max_profit = max(dfs(j, True), dfs(j, False) - prices[j], max_profit)

        return max_profit

    # Personal DP solution
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * (len(prices) + 2)
        sell = [0] * (len(prices) + 1)

        mx_buy = float('-inf')
        mx_sell = float('-inf')

        for i in range(len(prices) - 1, -1, -1):
            mx_buy = max(mx_buy, -prices[i], -prices[i] + sell[i + 1])
            buy[i] = mx_buy

            mx_sell = max(mx_sell, prices[i], prices[i] + buy[i + 2])
            sell[i] = mx_sell

        return max(buy)


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxProfit([1]))