class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        # code here
        V = len(adj)
        visited = [False] * V
        stack = [src]
        visited[src] = True

        while stack:
            node = stack.pop()

            if node == dest:
                return True

            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)

        return False        