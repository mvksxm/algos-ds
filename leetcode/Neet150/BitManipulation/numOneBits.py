
# My solution
# TC -> O(log(n)) or O(1) for a fixed bit integer.
# SC -> O(1)
# Approach
# While n != 0, shift 1 bit to the right and compare it with 0001 (number - 1). If resulting val is 1, increment count
# by 1. In the end, return count.

# Canonical solution
# k -> num of single bits in the n.
# TC -> O(k)
# SC -> O(1)
# Approach
# While n != 0, compare n with n - 1. It ensures that we are clearing the rightmost bit and not modifying anything
# after it. Increment count by 1 on each iteration of the while loop. In the end, return count.


class Solution:

    # My solution
    def hammingWeightShifting(self, n: int) -> int:
        count = 0

        while n:
            if n & 1 == 1: count += 1
            n >>= 1

        return count

    # Canonical
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count