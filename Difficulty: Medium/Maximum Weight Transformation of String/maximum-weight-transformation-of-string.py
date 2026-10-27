class Solution:
    def getMaxWeight(self, s):
        # code here
        n = len(s)
        if n == 0:
            return 0
        m = n - 1
        if m == 0:
            return 1
        w = [2 if s[i] != s[i + 1] else 1 for i in range(m)]
        if m == 1:
            return n + w[0]
        dp0 = 0
        dp1 = w[0]
        for i in range(1, m):
            dp2 = max(dp1, dp0 + w[i])
            dp0 = dp1
            dp1 = dp2
        return n + dp1