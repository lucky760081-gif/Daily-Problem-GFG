class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        # code here
        n, m = len(mat), len(mat[0])

        pref = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            row = 0
            for j in range(m):
                row += mat[i][j]
                pref[i + 1][j + 1] = pref[i][j + 1] + row

        def ones(r1, c1, r2, c2):
            return (
                pref[r2 + 1][c2 + 1]
                - pref[r1][c2 + 1]
                - pref[r2 + 1][c1]
                + pref[r1][c1]
            )

        ans = []

        for x, y in queries:
            max_r = min(x, y, n - 1 - x, m - 1 - y)

            if ones(x, y, x, y) > k:
                ans.append(-1)
                continue

            lo, hi = 0, max_r
            best = 0

            while lo <= hi:
                mid = (lo + hi) // 2

                r1, c1 = x - mid, y - mid
                r2, c2 = x + mid, y + mid

                if ones(r1, c1, r2, c2) <= k:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            ans.append(2 * best + 1)

        return ans