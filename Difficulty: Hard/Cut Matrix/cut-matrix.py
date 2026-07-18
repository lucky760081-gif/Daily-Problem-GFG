class Solution:
    def findWays(self, matrix, k):
        # code here
        MOD = 10**9 + 7
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        row_has = [[0] * m for _ in range(n)]
        for i in range(n):
            suffix = 0
            for j in range(m - 1, -1, -1):
                suffix |= matrix[i][j]
                row_has[i][j] = 1 if suffix else 0
        col_has = [[0] * m for _ in range(n)]
        for j in range(m):
            suffix = 0
            for i in range(n - 1, -1, -1):
                suffix |= matrix[i][j]
                col_has[i][j] = 1 if suffix else 0
        first_row = [[n] * m for _ in range(n)]
        for c in range(m):
            curr = n
            for r in range(n - 1, -1, -1):
                if row_has[r][c]:
                    curr = r
                first_row[r][c] = curr
        first_col = [[m] * m for _ in range(n)]
        for r in range(n):
            curr = m
            for c in range(m - 1, -1, -1):
                if col_has[r][c]:
                    curr = c
                first_col[r][c] = curr
        dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
        for r in range(n):
            for c in range(m):
                if first_row[r][c] < n:
                    dp[r][c][1] = 1
        for p in range(2, k + 1):
            horiz_suffix = [[0] * (n + 1) for _ in range(m + 1)]
            for c in range(m + 1):
                s = 0
                for rr in range(n, -1, -1):
                    if rr < n + 1:
                        s = (s + dp[rr][c][p - 1]) % MOD
                    horiz_suffix[c][rr] = s
            vert_suffix = [[0] * (m + 1) for _ in range(n + 1)]
            for r in range(n + 1):
                s = 0
                for cc in range(m, -1, -1):
                    if cc < m + 1:
                        s = (s + dp[r][cc][p - 1]) % MOD
                    vert_suffix[r][cc] = s
            for r in range(n):
                for c in range(m):
                    fr = first_row[r][c]
                    low = fr + 1
                    hsum = 0
                    if low <= n:
                        hsum = horiz_suffix[c][low]
                    fc = first_col[r][c]
                    lowc = fc + 1
                    vsum = 0
                    if lowc <= m:
                        vsum = vert_suffix[r][lowc]
                    dp[r][c][p] = (hsum + vsum) % MOD
        return dp[0][0][k]