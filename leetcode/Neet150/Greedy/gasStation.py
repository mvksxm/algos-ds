from typing import List

# TC -> O(n)
# SC -> O(1)

# Approach (Greedy)
# Maintain a cumulative variable - 'total', which contains a current amount of gas that we have in a tank. If balance
# drops to < 0. Set the result idx to 'i + 1' and set the 'total' variable to 0.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res_idx = 0
        for i in range(len(gas)):
            gas_needed = gas[i] - cost[i]

            if total + gas_needed < 0:
                res_idx = i + 1
                total = 0
            else:
                total += gas_needed

        return res_idx