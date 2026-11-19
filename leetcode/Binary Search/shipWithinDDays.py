
# TC -> O(n * log(max(weights))
# SC -> O(1)

class Solution:

    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def isSuitable(capacity):

            days_taken = 0
            occupied = 0

            for weight in weights:

                occupied += weight
                if occupied > capacity:
                    days_taken += 1
                    occupied = weight

                if days_taken > days: return False

            if occupied: days_taken += 1

            return days_taken <= days


        left = max(weights)
        right = sum(weights)
        answer = -1

        while left <= right:
            mid = left + (right - left) // 2

            if isSuitable(mid):
                right = mid - 1
                answer = mid
            else:
                left = mid + 1

        return answer