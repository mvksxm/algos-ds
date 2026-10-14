from collections import defaultdict, deque

# TC -> O(V + E)
# SC -> O(V + E)

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        conn_arr = [0] * n
        adjacency_list = defaultdict(list)

        for n1, n2 in edges:
            adjacency_list[n1].append(n2)
            adjacency_list[n2].append(n1)
            conn_arr[n1] += 1
            conn_arr[n2] += 1

        start_nodes = [i for i in range(len(conn_arr)) if conn_arr[i] <= 1]
        queue = deque(start_nodes)

        processed = 0
        while n - processed > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                processed += 1

                # mark as visited
                conn_arr[node] = 0
                for child in adjacency_list[node]:
                    conn_arr[child] -= 1
                    if conn_arr[child] == 1:
                        queue.append(child)

        return [n for n in queue]

if __name__ == "__main__":
    sln = Solution()
    print(sln.findMinHeightTrees(3, [[0,1],[0,2]]))