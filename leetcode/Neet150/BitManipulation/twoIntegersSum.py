class Solution:
    def getSum(self, a: int, b: int) -> int:

        res = 0
        iter_n = 0
        carry = 0


        bigger = a if a > b else b
        smaller = a if a < b else b

        while bigger:
            a_bit = bigger & 1
            b_bit = smaller & 1

            if a_bit and b_bit and carry:
                res |= (1 << iter_n)
                carry = 1
            elif (a_bit and b_bit) or (carry and (a_bit or b_bit)):
                res &= ~(1 << iter_n)
                carry = 1
            elif (carry and (not a_bit and not b_bit)) or (a_bit or b_bit):
                res |= (1 << iter_n)
                carry = 0
            else:
                res &= ~(1 << iter_n)

            bigger >>= 1
            smaller >>= 1
            iter_n += 1

        if carry:
            res |= (1 << iter_n)

        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.getSum(4, 7))
