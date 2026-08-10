import heapq
from collections import defaultdict, deque
from typing import List


# n -> len(tasks)
# TC -> O(n)
# SC -> O(1); At max we will add 26 characters to the queue and to the max heap, which can be rounded to O(1).

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_heap = []
        freq_map = defaultdict(int)
        cooldown_queue = deque()

        for task in tasks: freq_map[task] += 1

        for key, val in freq_map.items():
            heapq.heappush_max(task_heap, (val, key))

        slot = 1
        while cooldown_queue or task_heap:
            if cooldown_queue and cooldown_queue[0][1] <= slot:
                cooled_task_data = cooldown_queue.popleft()
                cooled_task = cooled_task_data[0]
                heapq.heappush_max(task_heap, (freq_map[cooled_task], cooled_task))
            elif task_heap:
                top_task = heapq.heappop_max(task_heap)
                freq_map[top_task[1]] -= 1
                if freq_map[top_task[1]] > 0:
                    cooldown_queue.append((top_task[1], slot + n + 1))
                slot += 1
            else:
                slot += 1


        return slot - 1

if __name__ == "__main__":
    sln = Solution()
    print(sln.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 1))