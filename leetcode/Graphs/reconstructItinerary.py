from typing import List
from collections import defaultdict
from tester import Tester


# Time Complexity: E * log(E) + E = O(E * log(E)), where E is the amount of edges (tickets)
# Space Complexity: O(E)

# Approach
# For each source airport, sort target airports lexicographically in ascending order and then execute the Eulerian Circuit
# algorithm on top of the map, which represents a graph.

class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []

        # Setting up dict
        graph_map = defaultdict(list)
        for ticket in tickets:
            source = ticket[0]
            dest = ticket[1]
            graph_map[source].append(dest)

        for key, val in graph_map.items():
            graph_map[key] = sorted(val)

        def dfs(node: str):
            edges = graph_map[node]

            for i in range(len(edges)):

                if edges[i] is None: continue

                next_node = edges[i]
                edges[i] = None

                dfs(next_node)

            if not any(edges):
                res.append(node)
                return


        dfs("JFK")
        return res[::-1]

    def findItineraryElegant(self, tickets: List[List[str]]) -> List[str]:

        # Adjacency list
        res = []
        sorted_tickets = sorted(tickets, reverse = True, key = lambda x: x[1])
        graph = defaultdict(list)
        for ticket in sorted_tickets:
            graph[ticket[0]].append(ticket[1])

        def dfs(airport: str):
            child_nodes = graph[airport]

            while child_nodes:
                c_node = child_nodes.pop()
                dfs(c_node)

            if not child_nodes: res.append(airport)


        dfs("JFK")
        return res[::-1]

if __name__ == "__main__":

    sln = Solution()
    tst = Tester()

    test_cases = [
        [
            [[
                 ["JFK","SFO"],
                 ["JFK","ATL"],
                 ["SFO","JFK"],
                 ["ATL","AAA"],
                 ["AAA","ATL"],
                 ["ATL","BBB"],
                 ["BBB","ATL"],
                 ["ATL","CCC"],
                 ["CCC","ATL"],
                 ["ATL","DDD"],
                 ["DDD","ATL"],
                 ["ATL","EEE"],
                 ["EEE","ATL"],
                 ["ATL","FFF"],
                 ["FFF","ATL"],
                 ["ATL","GGG"],
                 ["GGG","ATL"],
                 ["ATL","HHH"],
                 ["HHH","ATL"],
                 ["ATL","III"],
                 ["III","ATL"],
                 ["ATL","JJJ"],
                 ["JJJ","ATL"],
                 ["ATL","KKK"],
                 ["KKK","ATL"],
                 ["ATL","LLL"],
                 ["LLL","ATL"],
                 ["ATL","MMM"],
                 ["MMM","ATL"],
                 ["ATL","NNN"],
                 ["NNN","ATL"]
            ]],
            ["JFK","SFO","JFK","ATL","AAA","ATL","BBB","ATL","CCC","ATL","DDD","ATL","EEE","ATL","FFF","ATL","GGG","ATL","HHH","ATL","III","ATL","JJJ","ATL","KKK","ATL","LLL","ATL","MMM","ATL","NNN","ATL"]
        ]
    ]

    tst.array_test(test_cases, sln.findItinerary)