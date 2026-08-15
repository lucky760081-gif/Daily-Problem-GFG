class Solution:

    def countWithout(self, n: int, d: int) -> int:
        # code here
        s = str(n)
        m = len(s)
        dp = {}

        def dfs(pos, tight, started):
            if pos == m:
                return 1

            key = (pos, tight, started)
            if key in dp:
                return dp[key]

            limit = int(s[pos]) if tight else 9
            ans = 0

            for digit in range(limit + 1):
                ntight = tight and (digit == limit)

                if not started and digit == 0:
                    ans += dfs(pos + 1, ntight, False)
                else:
                    if digit != d:
                        ans += dfs(pos + 1, ntight, True)

            dp[key] = ans
            return ans

        return dfs(0, True, False) - 1