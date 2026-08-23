from collections import deque
class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])

        if mat[r][c] == '#':
            return 0

 

        INF = 10**18
        dist = [[INF] * m for _ in range(n)]

        dq = deque()
        dist[r][c] = 0
        dq.append((r, c))

        while dq:
            x, y = dq.popleft()

            # Left
            if y > 0 and mat[x][y - 1] == '.' and dist[x][y - 1] > dist[x][y]:
                dist[x][y - 1] = dist[x][y]
                dq.appendleft((x, y - 1))

            # Right
            if y + 1 < m and mat[x][y + 1] == '.' and dist[x][y + 1] > dist[x][y]:
                dist[x][y + 1] = dist[x][y]
                dq.appendleft((x, y + 1))

            # Up
            if x > 0 and mat[x - 1][y] == '.' and dist[x - 1][y] > dist[x][y] + 1:
                dist[x - 1][y] = dist[x][y] + 1
                dq.append((x - 1, y))

            # Down
            if x + 1 < n and mat[x + 1][y] == '.' and dist[x + 1][y] > dist[x][y]:
                dist[x + 1][y] = dist[x][y]
                dq.appendleft((x + 1, y))

        ans = 0

        for i in range(n):
            for j in range(m):
                if dist[i][j] == INF:
                    continue

                up = dist[i][j]
                down = up + (i - r)

                if up <= u and down <= d:
                    ans += 1

        return ans