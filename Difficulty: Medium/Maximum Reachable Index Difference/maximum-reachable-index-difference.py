class Solution:
    def maxIndexDifference(self, s):
        # code here
        n = len(s)

        best = [-1] * 26
        ans = -1

        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')

            dp = i
            if c < 25 and best[c + 1] != -1:
                dp = best[c + 1]

            best[c] = max(best[c], dp)

            if c == 0:
                ans = max(ans, dp - i)

        return ans