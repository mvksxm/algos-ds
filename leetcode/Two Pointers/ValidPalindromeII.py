
# Time Complexity: O(n+m), where m is the length of s[l_p:r_p+1], which was encountered during a mismatch.
# Space Complexity: O(2) = O(1). At worst case self.iteration() will be called 3 times, however recursion stack at max
# will be of length 2.

class Solution:

    def iteration(self, l_p, r_p,  s: str, is_deleted: bool) -> bool:

        while l_p < r_p:
            if s[l_p] != s[r_p] and is_deleted:
                return False

            if s[l_p] != s[r_p]:
                return self.iteration(l_p + 1, r_p, s, True) or self.iteration(l_p, r_p - 1, s, True)

            l_p += 1
            r_p -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        is_deleted = False

        l_p = 0
        r_p = len(s) - 1

        return self.iteration(l_p, r_p, s, is_deleted)


if __name__ == "__main__":
    tests = [
        ["aba", True],
        ["abba", True],
        ["abc", False],

        ["abca", True],
        ["deeee", True],
        ["raceacar", True],

        ["abcdef", False],
        ["abcda", False],

        ["a", True],
        ["", True],
        ["ab", True],

        ["cbbcc", True],
        ["aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True],

        ["abccdba", True],
        ["abcdcba", True],
        ["abcdecba", True],

        ["abecbea", False],
    ]
    sln = Solution()

    for test in tests:
        if not sln.validPalindrome(test[0]) == test[1]:
            print(f"Test case -> {test} did not pass!")

