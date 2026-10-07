
# n -> len(nums)
# TC -> O(n! * n)
# SC -> O(n) (not taking into consideration a returned array -> 'res')

# Approach:
# Backtracking with a frequency map.


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        freq_mp = {}
        for nm in nums:
            freq_mp[nm] = freq_mp.get(nm, 0) + 1


        res = []
        perm = []

        def dfs():

            if not freq_mp:
                res.append(perm.copy())
                return

            keys = list(freq_mp.keys())

            for k in keys:

                freq_mp[k] -= 1
                if freq_mp[k] == 0: del freq_mp[k]
                perm.append(k)

                dfs()

                freq_mp[k] = freq_mp.get(k, 0) + 1
                perm.pop()

        dfs()
        return res