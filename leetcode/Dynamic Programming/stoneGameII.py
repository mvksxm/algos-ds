
# TC -> O(n^3)
# SC -> O(n^2)

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        dp ={}

        piles_sm = sum(piles)
        piles_len = len(piles)

        def dfs(left_idx, limit, prev_sm):

            if left_idx >= piles_len: return 0

            if (left_idx, limit) in dp:
                return dp[(left_idx, limit)]

            optimal_sm = 0
            local_sm = 0

            for i in range(left_idx, left_idx + limit):
                if i >= piles_len:
                    break
                X = i - left_idx + 1
                local_sm += piles[i]
                another_turn = dfs(i + 1, max(limit, X * 2), prev_sm + local_sm)
                optimal_sm = max(optimal_sm, piles_sm - prev_sm - another_turn)

            dp[(left_idx, limit)] = optimal_sm
            return optimal_sm

        return dfs(0, 2, 0)
