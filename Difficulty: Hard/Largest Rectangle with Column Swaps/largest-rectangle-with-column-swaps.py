class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        heights = [0] * m
        ans = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            curr = sorted(heights, reverse=True)

            for j in range(m):
                ans = max(ans, curr[j] * (j + 1))

        return ans