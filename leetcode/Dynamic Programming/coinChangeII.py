from typing import List


class Solution:
    def recursiveChange(self, amount: int, coins: List[int]) -> int:

        """
        top-bottom approach
        """

        cache = {}

        def dfs(amnt: int, idx: int):

            # Base Cases
            if amnt == amount: return 1
            if amnt > amount: return 0


            combinations_count = 0
            for i in range(idx, len(coins)):

                child_combinations: int
                if (amnt, i) in cache:
                    child_combinations = cache[(amnt, i)]
                else:
                    child_combinations = dfs(amnt + coins[i], i)

                cache[(amnt, i)] = child_combinations
                combinations_count += child_combinations

            return combinations_count

        return dfs(0, 0)

    def change(self, amount: int, coins: List[int]) -> int:

        """
        DP approach
        """

        combinations_array = [1] + [0] * amount

        for coin in coins:
            for amnt in range(1, amount + 1):
                prev_idx = amnt - coin
                if 0 <= prev_idx < amount + 1:
                    combinations_array[amnt] = combinations_array[prev_idx] + combinations_array[amnt]

        return combinations_array[-1]


if __name__ == "__main__":

    sln = Solution()
    print(sln.change(5, [1, 2, 5]))