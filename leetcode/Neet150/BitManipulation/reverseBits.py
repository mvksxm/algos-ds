
# TC -> O(1), since n is a 32 bit integer
# SC -> O(1)

# Approach
# Shift the original n to the right while it's bigger than 0. Maintain the var -> curr_bit, which represents a
# currently unoccupied bit from the left side of the bit array. If 1 is encountered during shifting, put 2 to the power
# of curr_bit (2**curr_bit) and append the result to the 'res' variable. Such an operation simulates the process of
# setting the bit under a particular idx -> curr_bit. In the end, after 'n' becomes 0, return 'res'.

class Solution:
    def reverseBits(self, n: int) -> int:
        curr_bit = 31
        res = 0

        while n:
            if n & 1 == 1:
                res += 2**curr_bit

            curr_bit -= 1
            n >>= 1

        return res