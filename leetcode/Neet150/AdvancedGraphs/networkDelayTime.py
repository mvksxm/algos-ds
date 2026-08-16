from collections import defaultdict
from typing import List
import heapq

# Approach -> use Dijkstra to find min path to the last node in the graph and return it. In case if not all nodes were
# visited (len(visited_set) != n) -> return -1

# E -> edges; N -> nodes
# TC -> O(E*log(N))
# SC -> O(N + E)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited_set = set()
        adjacency_list = defaultdict(list)

        for time in times:
            adjacency_list[time[0]].append((time[1],time[2]))

        network_heap = [(0, k)]
        min_distance = 0

        distances = [float('inf')] * (n + 1)

        while network_heap:
            distance, node_id = heapq.heappop(network_heap)
            if node_id in visited_set: continue
            min_distance = distance
            visited_set.add(node_id)

            for c_node in adjacency_list[node_id]:
                c_node_id = c_node[0]
                c_distance = c_node[1] + distance
                if distances[c_node_id] > c_distance:
                    heapq.heappush(network_heap, (c_node[1] + distance, c_node[0]))
                    distances[c_node_id] = c_distance

        if len(visited_set) != n: return -1

        return min_distance