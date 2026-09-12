from typing import List


# TC -> O(n)
# SC -> O(1)

# Approach:
# Maintain a found array, which contains a bool under the index of a num in target. Iterate through the triplets array.
# If triplet encountered during an iteration is suitable (triplet is suitable, if it contains nums which are smaller
# or equal than the values in the target array.), check, which nums are equal in triplet and in the target array.
# In case, if some are equal set the bools under respective indeces in the found array to True. In the end, if all
# values in found are True -> return True.

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False] * 3

        for a, b, c in triplets:

            if not (a <= target[0] and b <= target[1] and c <= target[2]):
                continue

            found[0] = a == target[0] or found[0]
            found[1] = b == target[1] or found[1]
            found[2] = c == target[2] or found[2]

        return all(found)

if __name__ == "__main__":
    sln = Solution()
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    target = [2,7,5]
    print(sln.mergeTriplets(triplets, target))