from collections import defaultdict
from typing import List
import heapq

# Bellman-Ford algorithm.
# m -> edges
# n -> nodes in the graph
# TC -> O(k * (m + n))
# SC -> O(n)


# Dijkstra algorithm.
# TC -> O(e * log(k * e))
# SC -> O(n × k + e)

class Solution:

    # Bellman-Ford algorithm.
    def findCheapestPriceBF(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        path_lens = [float('inf')] * n
        path_lens[src] = 0
        max_edges = k + 1

        for _ in range(max_edges):
            t_path_lens = path_lens.copy()
            for flight in flights:

                t_cost = path_lens[flight[0]] + flight[2]

                if t_cost < t_path_lens[flight[1]]:
                    t_path_lens[flight[1]] = t_cost

            path_lens = t_path_lens

        if path_lens[dst] == float('inf'):
            return -1

        return path_lens[dst]

    # Dijkstra algorithm
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency_list = defaultdict(list)
        for flight in flights:
            adjacency_list[flight[0]].append((flight[1], flight[2]))

        min_heap = [(0, -1, src)]
        stops_map = {}

        while min_heap:
            top_elem = heapq.heappop(min_heap)
            cost, stops, port = top_elem

            if port == dst: return cost

            u_stops = stops + 1
            if u_stops > k: continue

            composite_key = (port, u_stops)
            if composite_key not in stops_map or stops_map[composite_key] > cost:
                stops_map[composite_key] = cost
                for c_port in adjacency_list[port]:
                    heapq.heappush(min_heap, (cost + c_port[1], u_stops, c_port[0]))

        return -1

if __name__ == "__main__":
    n=4
    flights=[[0,1,200],[1,2,100],[1,3,300],[2,3,100]]
    src=0
    dst=3
    k=1

    sln = Solution()
    print(sln.findCheapestPrice(n, flights, src, dst, k))
