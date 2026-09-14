from collections import deque
class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])

        safe = [[True] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = False
                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = False

        q = deque()

        for i in range(n):
            if safe[i][0]:
                q.append((i, 0, 1))
                safe[i][0] = False

        while q:
            i, j, d = q.popleft()

            if j == m - 1:
                return d

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < n and 0 <= nj < m and safe[ni][nj]:
                    safe[ni][nj] = False
                    q.append((ni, nj, d + 1))

        return -1        