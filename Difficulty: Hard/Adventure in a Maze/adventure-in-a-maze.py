class Solution:
    def findWays(self, grid):
        # code here
        MOD = 1000000007
        n = len(grid)

        ways = [[0] * n for _ in range(n)]
        adv = [[-1] * n for _ in range(n)]

        ways[n - 1][n - 1] = 1
        adv[n - 1][n - 1] = grid[n - 1][n - 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue

                cnt = 0
                best = -1

                if grid[i][j] in (1, 3) and j + 1 < n:
                    cnt = (cnt + ways[i][j + 1]) % MOD
                    if adv[i][j + 1] != -1:
                        best = max(best, adv[i][j + 1] + grid[i][j])

                if grid[i][j] in (2, 3) and i + 1 < n:
                    cnt = (cnt + ways[i + 1][j]) % MOD
                    if adv[i + 1][j] != -1:
                        best = max(best, adv[i + 1][j] + grid[i][j])

                ways[i][j] = cnt
                adv[i][j] = best

        if ways[0][0] == 0:
            return [0, 0]

        return [ways[0][0], adv[0][0]]