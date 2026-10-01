
# n -> len(startTime) = len(endTime) = len(profit)
# TC -> O(n * log(n)) (sorting) + O(n * log(n)) (final iteration with Binary Search)
# SC -> O(n)
# Approach: sort the input data in ascending order by startTime, then iterate backwards and on every job
# check if it should be skipped (and next one should be considered instead), added by itself or added with the job that is
# scheduled after the end time of the current one. Decision with which option to proceed is made according to the biggest
# profit that was encountered so far.

class Solution:
    # find the first with start time bigger than or equal to end time
    def binary_search(self, target, arr):

        target_i = -1

        l_p = 0
        r_p = len(arr) - 1
        while l_p <= r_p:
            pivot = l_p + (r_p - l_p) // 2
            start, end, _ = arr[pivot]
            if start >= target:
                target_i = pivot
                r_p = pivot - 1
            else:
                l_p = pivot + 1

        return target_i



    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        n = len(startTime)
        dp = [0] * n

        unified_ds = [[startTime[i], endTime[i], profit[i]] for i in range(len(startTime))]
        unified_ds.sort(key = lambda x: x[0])

        for i in range(len(unified_ds)-1, -1, -1):
            job = unified_ds[i]
            non_overlap_i = self.binary_search(job[1],unified_ds )
            prf = job[2]
            if non_overlap_i != -1:
                prf += dp[non_overlap_i]

            if i < n - 1:
                prf = max(prf, dp[i + 1])

            dp[i] = prf

        return dp[0]

if __name__ == "__main__":
    sln = Solution()
    print(sln.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
