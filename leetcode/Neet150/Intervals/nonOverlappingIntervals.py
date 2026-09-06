from typing import List

# n -> len(intervals)
# TC -> O(n * log(n))
# SC -> O(n)

# Approach:
# Sort the intervals by first and second values. Then iterate through the sorted array. If non overlapping encountered -
# - change the curr interval to a newly encountered one and proceed with the iteration. If overlapping encountered
# increment to_delete by 1. Also, in case if overlapping has a second value smaller than the curr interval change curr
# interval to the newly encountered one (We do it, because there is a higher chance that we will encounter a non-overlapping
# interval, if the second value is smaller).



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals_sorted = sorted(intervals, key = lambda x: (x[0], x[1]))
        curr_interval = intervals_sorted[0]
        to_delete = 0

        for i in range(1, len(intervals_sorted)):

            # Non-Overlapping
            if intervals_sorted[i][0] >= curr_interval[1]:
                curr_interval = intervals_sorted[i]
                continue

            if intervals_sorted[i][1] <= curr_interval[1]:
                curr_interval = intervals_sorted[i]

            to_delete += 1

        return to_delete

if __name__ == "__main__":
    sln = Solution()
    print(sln.eraseOverlapIntervals([[1,2]]))