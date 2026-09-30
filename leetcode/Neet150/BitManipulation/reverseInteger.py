class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        num = abs(x)

        while num > 0:
            if res > 2**31 - 1 or res < -2**31: return 0
            div = num // 10
            res += num % (div * 10) if div > 0 else num
            res *= 10
            num = div

        final_res = res // 10
        if x < 0:
            return -final_res


        return final_res

if __name__ == "__main__":
    sln = Solution()
    print(sln.reverse(1234236467))