from collections import defaultdict
import heapq
from typing import List, Dict

# Implementation of the dijkstra algorithm
# N -> amount of nodes in the graph; E -> amount of edges
# TC -> O((N+E) * log(N))
# SC -> O(N)


def dijkstra(n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    path_map = {}
    adjacency_list = defaultdict(list)

    for i in range(n):
        path_map[i] = -1 if i != src else 0

    for edge in edges:
        adjacency_list[edge[0]].append((edge[2], edge[1]))

    visited_set = {src}
    min_heap = [conn for conn in  adjacency_list[src]]
    heapq.heapify(min_heap)

    while min_heap:
        top_element = heapq.heappop(min_heap)
        weight, idx = top_element

        if idx not in visited_set:
            path_map[idx] = weight
            for child in adjacency_list[idx]:
                heapq.heappush(min_heap, (child[0] + weight, child[1]))
            visited_set.add(idx)

    return path_map