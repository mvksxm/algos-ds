# n -> len(num1); m -> len(num2)
# TC -> O(n*m)
# SC -> O(n+m)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = ["0"] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):

            bring_forward = 0

            for j in range(len(num2)-1, -1, -1):
                mod_idx = (len(num1)-1 - i) + (len(num2)-1 - j)
                prod = int(num1[i]) * int(num2[j])
                sm_prod = int(res[mod_idx]) + prod + bring_forward
                res[mod_idx] = str(sm_prod % 10)
                bring_forward= sm_prod // 10

            if bring_forward > 0:
                res[len(num2) + len(num1)-1 - i] = str(bring_forward + int(res[len(num2) + len(num1)-1 - i]))

        res = res[::-1]
        i = 0
        while i < len(res) and res[i] == "0":
            i += 1

        return "".join(res[i:])

if __name__ == "__main__":
    sln = Solution()
    print(sln.multiply("123", "456"))