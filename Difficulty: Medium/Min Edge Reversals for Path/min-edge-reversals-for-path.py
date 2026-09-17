class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        # code here
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        dist = [10**9] * (n + 1)
        dist[src] = 0

        dq = deque([src])

        while dq:
            u = dq.popleft()

            for v, cost in graph[u]:
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost

                    if cost == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)

        return -1 if dist[dst] == 10**9 else dist[dst]                