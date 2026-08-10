class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # code here
        n = len(h)

        dp0 = 0
        dp1 = l[0]
        dp2 = h[0]

        for i in range(1, n):
            ndp0 = max(dp0, dp1, dp2)
            ndp1 = max(dp0, dp1, dp2) + l[i]
            ndp2 = dp0 + h[i]

            dp0, dp1, dp2 = ndp0, ndp1, ndp2

        return max(dp0, dp1, dp2)