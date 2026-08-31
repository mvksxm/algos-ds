
# Approach:
# Each substring has either one char center or two char center. In order to get all the palindromes, we need to
# iterate through the input string and assume each char is a center. Also, in case if a particular char under the idx: i,
# is equal to the char under the idx: i + 1, we can formulate a 'double center' whose boundaries are i and i + 1
# and expand pointers from it as well. Important, when creating a double center, we need to make sure that we increment
# res by 1, since double center is a palindrome as well.
#
# Left pointer for single and double centers is starting from the left_center_boundary - 1
# and expanding to the left. Right pointer is starting from right_center_boundary + 1 and expanding to the right.
# In case if left_pointer == right_pointer -> incrementing res by 1, otherwise breaking the while loop and proceeding
# further to the next center by using a for loop.

# TC -> O(n^2)
# SC -> O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            pointers = [
                (i - 1, i + 1)
            ]
            res += 1

            if i + 1 < len(s) and s[i + 1] == s[i]:
                res += 1
                pointers.append((i - 1, i + 2))

            for l_p, r_p in pointers:
                while l_p >= 0 and r_p < len(s):

                    if s[l_p] == s[r_p]:
                        res += 1
                    else:
                        break

                    l_p -= 1
                    r_p += 1

        return res
