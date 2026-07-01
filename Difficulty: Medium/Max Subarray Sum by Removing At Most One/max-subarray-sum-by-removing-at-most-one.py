class Solution:
    def maxSumSubarray(self, arr):
        # code here
        n = len(arr)

        if n == 1:
            return arr[0]

        fw = [0] * n
        bw = [0] * n

        fw[0] = arr[0]
        ans = arr[0]

        for i in range(1, n):
            fw[i] = max(arr[i], fw[i - 1] + arr[i])
            ans = max(ans, fw[i])

        bw[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            bw[i] = max(arr[i], bw[i + 1] + arr[i])

        for i in range(1, n - 1):
            ans = max(ans, fw[i - 1] + bw[i + 1])

        return ans