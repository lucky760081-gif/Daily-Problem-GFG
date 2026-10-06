class Solution:
    def longIncPath(self, matrix, n, m):
        # code here
        n = len(matrix)
        m = len(matrix[0])
        total = n * m

        from array import array

        dp = array('I', [1]) * total
        cells = list(range(total))
        cells.sort(key=lambda x: matrix[x // m][x % m])

        ans = 1

        for idx in cells:
            r = idx // m
            c = idx - r * m
            val = matrix[r][c]
            best = 1

            if r > 0 and matrix[r - 1][c] < val:
                best = max(best, dp[idx - m] + 1)

            if r + 1 < n and matrix[r + 1][c] < val:
                best = max(best, dp[idx + m] + 1)

            if c > 0 and matrix[r][c - 1] < val:
                best = max(best, dp[idx - 1] + 1)

            if c + 1 < m and matrix[r][c + 1] < val:
                best = max(best, dp[idx + 1] + 1)

            dp[idx] = best
            ans = max(ans, best)

        return ans