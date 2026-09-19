# TC -> O(log(n))
# SC -> O(log(n))

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n

        while curr not in seen:
            seen.add(curr)

            new = 0
            while curr > 0:
                rounded = (curr // 10) * 10
                new += (curr % rounded)**2 if rounded != 0 else curr**2
                curr = curr // 10

            if new == 1: return True
            curr = new

        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.isHappy(19))