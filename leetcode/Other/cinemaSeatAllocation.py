from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        res = 0

        allowed_slots = [
            (2,5),
            (4,7),
            (6,9)
        ]

        slots_copy = allowed_slots.copy()

        reservedSeats.sort(key=lambda x: x[0])
        c_processed = 0
        last_processed_r = reservedSeats[0][0]
        for i in range(len(reservedSeats) + 1):
            s = reservedSeats[i][1] if i < len(reservedSeats) else float('inf')
            r = reservedSeats[i][0] if i < len(reservedSeats) else float('inf')
            if r != last_processed_r:
                local_res = 0
                l_success_idx = -2
                for i in range(len(slots_copy)):
                    if slots_copy[i] and i - l_success_idx >= 2:
                        local_res += 1
                        l_success_idx = i

                res += local_res
                slots_copy = allowed_slots.copy()
                c_processed += 1
                last_processed_r = r

            for j in range(len(slots_copy)):
                if slots_copy[j] and slots_copy[j][0] <= s <= slots_copy[j][1]:
                    slots_copy[j] = None

        return res + (n - c_processed) * 2


if __name__ == "__main__":
    sln = Solution()
    n = 2
    reservedSeats = [[2,1],[1,8],[2,6]]
    print(sln.maxNumberOfFamilies(n, reservedSeats))