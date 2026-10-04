class Solution:
    def findPerimeter(self, mat):
        # code here        
        n = len(mat)
        m = len(mat[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    ans += 4

                    if i > 0 and mat[i - 1][j] == 1:
                        ans -= 2

                    if j > 0 and mat[i][j - 1] == 1:
                        ans -= 2

        return ans