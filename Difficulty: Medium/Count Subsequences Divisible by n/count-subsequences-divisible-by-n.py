class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 1000000007
        dp = [0] * n

        for ch in s:
            digit = ord(ch) - ord('0')
            ndp = dp[:]

            ndp[digit % n] = (ndp[digit % n] + 1) % MOD

            for r in range(n):
                nr = (r * 10 + digit) % n
                ndp[nr] = (ndp[nr] + dp[r]) % MOD

            dp = ndp

        return dp[0]