class Solution:
    def zigzagSequence(self, mat):
        # code here
        n = len(mat)

        dp = mat[0][:]

        for i in range(1, n):
            new_dp = [0] * n

            max1 = max2 = -1
            idx1 = -1

            for j in range(n):
                if dp[j] > max1:
                    max2 = max1
                    max1 = dp[j]
                    idx1 = j
                elif dp[j] > max2:
                    max2 = dp[j]

            for j in range(n):
                best_prev = max2 if j == idx1 else max1
                new_dp[j] = mat[i][j] + best_prev

            dp = new_dp

        return max(dp)