from typing import List
import collections
from collections import deque


# B -> number of buses; S -> average amount of stations per bus
# TC: O(B*S)
# SC: O(B*S)

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        station_bus_map = collections.defaultdict(list)

        for bus, stops in enumerate(routes):
            for stop in stops: station_bus_map[stop].append(bus)

        visited_buses = set()
        visited_stops = set()

        q = deque([(source, 0)])

        while q:
            stop_id, bus_count = q.popleft()
            if stop_id == target: return bus_count

            for bus in station_bus_map[stop_id]:
                if bus not in visited_buses:
                    visited_buses.add(bus)

                    for stop in routes[bus]:
                        if stop not in visited_stops:
                            q.append((stop, bus_count + 1))

        return -1