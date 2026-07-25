class Solution:
    def maximumSum(self, mat, k):
        # code here
        n = len(mat)

        pref = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )

        ans = float("-inf")

        for i in range(n - k + 1):
            for j in range(n - k + 1):
                s = (
                    pref[i + k][j + k]
                    - pref[i][j + k]
                    - pref[i + k][j]
                    + pref[i][j]
                )
                ans = max(ans, s)

        return ans