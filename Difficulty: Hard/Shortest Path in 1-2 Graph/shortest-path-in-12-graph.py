from collections import deque
class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # code here
        n = V + len(edges)
        adj = [[] for _ in range(n)]
        nxt = V

        for u, v, w in edges:
            if w == 1:
                adj[u].append(v)
                adj[v].append(u)
            else:
                x = nxt
                nxt += 1
                adj[u].append(x)
                adj[x].append(v)
                adj[v].append(x)
                adj[x].append(u)

        dist = [-1] * nxt
        q = deque([src])
        dist[src] = 0

        while q:
            u = q.popleft()
            if u == dest:
                return dist[u]
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

        return -1