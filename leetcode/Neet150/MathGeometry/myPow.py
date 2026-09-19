
# TC -> O(log(n))
# SC -> O(log(n))

# Approach
# Perform a recursive pow() operation. Specifically, on each recursive call -> divide n by two and then perform a child
# recursive call on a half only. Once recursive call for the half returns -> it will bring the number, which is equal
# to x^(n//2). Right after, in case if n is even -> we can multiply x^(n//2) by x^(n//2) and we will get a x^n. In
# case if n is odd and more than 0 -> we can multiply x^(n//2) * x^(n//2) * x. Finally, in case if n is odd and smaller
# than 0, we are performing x^(n//2) * x^(n//2) * 1/x.

class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if n == -1: return 1 / x

        divided_n = n // 2 if n > 0 else -(n // -2)
        half = self.myPow(x, divided_n)

        if half >= 10**4 or half <= -10**4: return half

        if n % 2 == 0:
            res = half * half
        elif n > 0:
            res = half * (half * x)
        else:
            res = half * (half * 1 / x)

        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.myPow(2.00000, -2147483648))