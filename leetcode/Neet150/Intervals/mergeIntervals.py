from typing import List

# n -> len(intervals)
# TC -> O(n*log(n))
# SC -> O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key = lambda x: (x[0], x[1]))

        res = []
        curr_interval = intervals_sorted[0]
        for i in range(len(intervals_sorted)):
            observed_interval = intervals_sorted[i]

            if curr_interval[1] < observed_interval[0]:
                res.append(curr_interval)
                curr_interval = observed_interval
            else:
                curr_interval[0] = min(curr_interval[0], observed_interval[0])
                curr_interval[1] = max(curr_interval[1], observed_interval[1])

        res.append(curr_interval)
        return res