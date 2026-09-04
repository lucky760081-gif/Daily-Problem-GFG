class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)

        if m >= n:
            return sum(arr)

        window = sum(arr[:m])
        ans = window

        for i in range(m, n + m - 1):
            window += arr[i % n] - arr[(i - m) % n]
            ans = max(ans, window)

        return ans