class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        # Optimal Solution
        dp = [0] * (n + 2)

        dp[1] = i

        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + i

            if x % 2 == 0:
                dp[x] = min(dp[x], dp[x // 2] + c)
            else:
                dp[x] = min(dp[x], dp[(x + 1) // 2] + c + d)

        return dp[n]
        
        
        
        
        
        
        
        
        
        # memo = {}

        # def solve(x):
        #     if x == 0:
        #         return 0

        #     if x == 1:
        #         return i

        #     if x in memo:
        #         return memo[x]

        #     ans = solve(x - 1) + i

        #     if x % 2 == 0:
        #         ans = min(ans, solve(x // 2) + c)
        #     else:
        #         ans = min(ans, solve((x + 1) // 2) + c + d)

        #     memo[x] = ans
        #     return ans

        # return solve(n)