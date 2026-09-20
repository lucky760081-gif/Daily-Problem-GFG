class Solution:
    def largestSubsquare(self, mat):
        # code here
        n = len(mat)

        right = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = 1
                    down[i][j] = 1

                    if j + 1 < n:
                        right[i][j] += right[i][j + 1]

                    if i + 1 < n:
                        down[i][j] += down[i + 1][j]

        ans = 0

        for i in range(n):
            for j in range(n):
                max_size = min(right[i][j], down[i][j])

                for size in range(max_size, ans, -1):
                    r = i + size - 1
                    c = j + size - 1

                    if r < n and c < n:
                        if right[r][j] >= size and down[i][c] >= size:
                            ans = size
                            break

        return ans        