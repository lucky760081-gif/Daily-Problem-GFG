class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        # code here
        INF = 10**9
        max_area = x + max(s, m, l)

        dp = [INF] * (max_area + 1)
        dp[0] = 0

        for area in range(max_area + 1):
            if dp[area] == INF:
                continue

            if area + s <= max_area:
                dp[area + s] = min(dp[area + s], dp[area] + cs)

            if area + m <= max_area:
                dp[area + m] = min(dp[area + m], dp[area] + cm)

            if area + l <= max_area:
                dp[area + l] = min(dp[area + l], dp[area] + cl)

        return min(dp[x:])