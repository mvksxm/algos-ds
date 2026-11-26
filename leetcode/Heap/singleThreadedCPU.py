import heapq

# n -> len(tasks)
# TC -> O(n * log(n))
# SC -> O(n)

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        main_heap = []
        curr_tasks_heap = []
        res = []
        curr_time = 1

        for i in range(len(tasks)):
            task = tasks[i]
            heapq.heappush(main_heap, (task[0], task[1], i))

        while main_heap or curr_tasks_heap:

            while main_heap:
                eTime, pTime, idx = main_heap[0]
                if eTime > curr_time: break
                heapq.heappop(main_heap)
                heapq.heappush(curr_tasks_heap, (pTime, idx))

            next_task = heapq.heappop(curr_tasks_heap) if curr_tasks_heap else None
            if next_task:
                res.append(next_task[1])
                curr_time += next_task[0]
            else:
                curr_time = main_heap[0][0] if main_heap else float('-inf')

        return res