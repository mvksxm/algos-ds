from typing import List

# TC -> O(n)
# SC -> O(1)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for r_p in range(len(arr)):
            if r_p - k < 0: continue

            curr_abs = abs(arr[r_p] - x)
            left_abs = abs(arr[r_p - k] - x)

            if curr_abs > left_abs or (curr_abs == left_abs and arr[r_p] > arr[r_p - k]):
                return arr[r_p - k:r_p]

        return arr[r_p + 1 - k: r_p + 1]