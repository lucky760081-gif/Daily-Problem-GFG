class Solution:
    def minSquares(self, n, m):
        # code here
        ans = 0

        while n > 0 and m > 0:
            if n > m:
                n, m = m, n

            count = m // n
            ans += count
            m = m % n

            if m == 0:
                break

        return ans        