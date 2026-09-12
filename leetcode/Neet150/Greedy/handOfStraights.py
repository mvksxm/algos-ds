from collections import defaultdict, deque
from typing import List

# Solution with a frequency map and recursion
# n -> len(hand)
# TC -> O(n * log(n))
# SC -> O(n)

# Approach
# Sort the hand array. Create a frequency map with the count of nums from the hand array. Iterate through the sorted
# hand and for each num execute the dfs() method that will check if it's possible to get the group of len 'groupSize'
# starting from the current num. dfs() will decrease the count of num in the frequency map by 1 and then will try to get
# the next_num (num + 1) from the map and, in case if it succeeds -> recursion continues, otherwise False is
# returned right away. If we are reaching a curr_count == groupSize during a recursion - it means that group was found, so
# we can return - 'True'. We are counting the amount of times, when dfs() returned True and, in case, if it equals to
# len(hand) // groupSize -> returning 'True' as the answer, otherwise - 'False'.
# Because we are decrementing the count of a num on each visit, it's guaranteed that each num will not be visited more
# than once. So, TC will be equal to O(n * log(n)) + O(n) = O(n * log(n))


# Canonical greedy solution with a frequency map
# n -> len(hand)
# TC -> O(n * log(n))
# SC -> O(n)

# Approach
# Sort the hand array. Create a frequency map with the count of nums from the hand array. Iterate through the sorted
# hand and for each num iterate through range(num, num + groupSize). On each next element - 'n' decrement freq_map[n]
# by 1. In case if n is already n -> return False. If iteration was completed without returning False, return True
# in the end.

class Solution:
    # My solution with a frequency map and recursion.
    def isNStraightHandRecursive(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand.sort()
        mp = defaultdict(int)

        for num in hand:
            mp[num] += 1

        def dfs(num, curr_count):

            if curr_count == groupSize:
                return True

            if mp[num] == 0:
                return False

            mp[num] -= 1

            next_num = num + 1
            return dfs(next_num, curr_count + 1)


        group_amt = 0
        for num in hand:
            if dfs(num, 0):
                group_amt += 1

        return group_amt == len(hand) // groupSize

    # Queue-based solution (My implementation)
    def isNStraightHandQueue(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand.sort()
        queue = deque()
        group_amount = 0
        i = 0

        while i < len(hand):

            if not queue:
                queue.append((hand[i], 1))
                i += 1
                continue

            initial_elem, count = queue.popleft()
            if count == groupSize:
                group_amount += 1
                continue

            while i < len(hand) and hand[i] == initial_elem:
                queue.append((hand[i], 1))
                i += 1

            if i < len(hand) and hand[i] - initial_elem == 1:
                queue.append((hand[i], count + 1))
                i += 1
            else:
                return False

        while queue:
            _, count = queue.popleft()
            if count == groupSize: group_amount += 1

        return group_amount == len(hand) // groupSize

    # Canonical Greedy
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq_map = defaultdict(int)
        for num in hand:
            freq_map[num] += 1

        for num in hand:
            if freq_map[num] == 0: continue
            for n in range(num, num + groupSize):
                if freq_map[n] == 0: return False
                freq_map[n] -= 1

        return True

if __name__ == "__main__":
    sln = Solution()
    hand = [1,2,2,3,3,4,6,7,8]
    # [3:2, 4:3]
    groupSize = 3
    print(sln.isNStraightHand(hand, groupSize))