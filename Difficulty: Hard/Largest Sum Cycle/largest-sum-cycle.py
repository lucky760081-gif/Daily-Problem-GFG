class Solution:
    def largestSumCycle(self, edge):
        # code here
        n = len(edge)
        visited = [0] * n
        ans = -1

        for i in range(n):
            if visited[i]:
                continue

            path = []
            pos = {}
            u = i

            while u != -1 and not visited[u]:
                visited[u] = 1
                pos[u] = len(path)
                path.append(u)
                u = edge[u]

            if u in pos:
                ans = max(ans, sum(path[pos[u]:]))

        return ans