
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        cache = {}
        def dp(level: int, target_dp: int):

            if target_dp == 0 and level == n:
                return 1

            if level > n or target_dp < 0:
                return 0

            cache_key = (level, target_dp)
            if cache_key in cache:
                amount_combinations = cache[cache_key]
                return amount_combinations

            sm = 0
            for side in range(1, k+1):
                sm = (sm + dp(level + 1, target_dp - side)) % MOD

            cache[cache_key] = sm

            return sm

        dice_combinations = dp(0, target)
        return dice_combinations


if __name__ == "__main__":
    sln = Solution()
    print(sln.numRollsToTarget(3, 6, 6 ))