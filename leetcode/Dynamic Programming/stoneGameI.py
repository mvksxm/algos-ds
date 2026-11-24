
# TC -> O(n^2)
# SC -> O(n^2)

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        dp = {}

        def dfs(start_idx, end_idx):

            # base case
            if start_idx == end_idx:
                return piles[start_idx], 0

            if (start_idx, end_idx) in dp:
                return dp[(start_idx, end_idx)]

            left_pick = piles[start_idx]
            another_sum1, this_sum1 = dfs(start_idx + 1, end_idx)

            right_pick = piles[end_idx]
            another_sum2, this_sum2 = dfs(start_idx, end_idx - 1)

            if left_pick + this_sum1 > right_pick + this_sum2:
                dp[(start_idx, end_idx)] = (left_pick + this_sum1, another_sum1)
                return left_pick + this_sum1, another_sum1

            dp[(start_idx, end_idx)] = (right_pick + this_sum2, another_sum2)

            return right_pick + this_sum2, another_sum2

        alice, bob = dfs(0, len(piles) - 1)
        return alice > bob