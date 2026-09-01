class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 1000000007
        ans = 0
        perm = 1

        for length in range(1, n + 1):
            if length % 2 == 0:
                p = length // 2

                if p == 1:
                    perm = k
                elif p <= k:
                    perm = perm * (k - p + 1) % MOD

                if p <= k:
                    ans = (ans + perm) % MOD
            else:
                p = length // 2

                if p == 0:
                    ways = k
                else:
                    ways = k
                    for j in range(p):
                        ways = ways * (k - 1 - j) % MOD

                ans = (ans + ways) % MOD

        return ans