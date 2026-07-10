class Solution:
    def getCount(self, n):
        # code here 
        ans = 0
        k = 2

        while k * (k + 1) // 2 <= n:
            t = n - k * (k - 1) // 2
            if t > 0 and t % k == 0:
                ans += 1
            k += 1

        return ans