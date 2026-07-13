class Solution:
    def minOperations(self, b):
        # code here
        MOD = 10**9 + 7
        n = len(b)

        vis = [False] * n
        lcm = 1

        def gcd(a, c):
            while c:
                a, c = c, a % c
            return a

        for i in range(n):
            if not vis[i]:
                cur = i
                cnt = 0
                while not vis[cur]:
                    vis[cur] = True
                    cur = b[cur] - 1
                    cnt += 1
                lcm = (lcm * cnt // gcd(lcm, cnt)) % MOD

        return lcm