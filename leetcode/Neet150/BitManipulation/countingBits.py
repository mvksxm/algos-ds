
# TC -> O(n)
# SC -> O(n)
# Approach
# Maintain a 'mid_num' variable, which will be containing numbers, that can be computed, when putting 2 to the power of x.
# In case, if num in range n is not equal to the mid_num * 2, it means that we are still in the window between mid_num
# and the next mid_num. For nums, which are a part of this window execute the following formula to count bits ->
# c_bits = res[mid_num] + res[i - mid_num]. For example, for 111 == 7 we will get 3 bits, because 100 == 4 (1 bit) +
# 11 == (7 - 4 = 3) (2 bits).

class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []

        for i in range(2):
            if i <= n and i == 0: res.append(0)
            if i <= n and i == 1: res.append(1)

        mid_num = 1
        for i in range(2, n + 1):
            if i == mid_num * 2:
                mid_num *= 2
                res.append(1)
            else:
                res.append(res[mid_num] + res[i - mid_num])

        return res