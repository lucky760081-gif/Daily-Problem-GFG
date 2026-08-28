class Solution:

    def minCost(self, mat):
        """code here"""
        a, b, c = mat[0]

        for i in range(1, len(mat)):
            x, y, z = mat[i]

            na = x + min(b, c)
            nb = y + min(a, c)
            nc = z + min(a, b)

            a, b, c = na, nb, nc

        return min(a, b, c)