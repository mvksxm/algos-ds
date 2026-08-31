

# Approach: use the center expansion logic. Specifically, choose an index in the middle of a particular substring,
# define left_pointer = i - 1 and right_pointer = i + 1. Expand left and right pointers while they are equal. Once, they
# are not update global res indexes, in case if substring, which was found during the current iteration is bigger than
# the biggest one, which was found previously. Also, in case if there are multiple adjacent characters, which are equal
# to current i, we need to make sure that left pointer and right pointer are the first chars, from left and right respectively,
# which are not equal to i, since substring, which contains only chars equal to i should be considered as 'center'. And
# we should expand pointers from the boundaries of the center only.

# CANONICAL IMPROVEMENT: since every substr can have either single center (odd len) or double center (even len), we can perform center expansion
# logic only for centers with len = 1 and for centers with len = 2. NOTE: center with len = 2 is valid only if both
# characters there are equal.

# TC -> O(n^2)
# SC -> O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = float("-inf")

        res_l_p = -1
        res_r_p = -1

        for i in range(len(s)):
            l_p = i - 1
            r_p = i + 1

            curr_len = 1

            while l_p >= 0 and s[i] == s[l_p]:
                curr_len += 1
                l_p -= 1

            while r_p < len(s) and s[i] == s[r_p]:
                curr_len += 1
                r_p += 1

            while l_p >= 0 and r_p < len(s):

                if s[l_p] == s[r_p]:
                    curr_len += 2
                else:
                    break

                l_p -= 1
                r_p += 1

            if curr_len > max_len:
                max_len = curr_len
                res_l_p = l_p + 1
                res_r_p = r_p

        return s[res_l_p:res_r_p]

if __name__ == "__main__":
    sln = Solution()
    s = "ababd"
    print(sln.longestPalindrome(s))