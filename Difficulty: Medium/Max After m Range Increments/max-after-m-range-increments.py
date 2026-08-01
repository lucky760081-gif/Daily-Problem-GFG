class Solution:
    def findMax(self, n, a, b, k):
        # code here
        diff = [0] * (n + 1)

        for l, r, val in zip(a, b, k):
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val

        cur = 0
        ans = 0

        for i in range(n):
            cur += diff[i]
            ans = max(ans, cur)

        return ans