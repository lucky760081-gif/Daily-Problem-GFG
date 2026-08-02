class Solution:
    def count(self, n: int, m: int) -> int:
        # code here
        MOD = 10**9 + 7

        adj = [[] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if i % j == 0 or j % i == 0:
                    adj[i].append(j)

        dp = [1] * (m + 1)

        for _ in range(2, n + 1):
            ndp = [0] * (m + 1)

            for i in range(1, m + 1):
                for j in adj[i]:
                    ndp[i] = (ndp[i] + dp[j]) % MOD

            dp = ndp

        return sum(dp[1:]) % MOD