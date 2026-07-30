class Solution:
    def maxSubsetXOR(self, arr):
        # code here
        n = len(arr)
        idx = 0

        for bit in range(31, -1, -1):
            mx = -1

            for i in range(idx, n):
                if arr[i] & (1 << bit):
                    mx = i
                    break

            if mx == -1:
                continue

            for i in range(idx + 1, n):
                if (arr[i] & (1 << bit)) and arr[i] > arr[mx]:
                    mx = i

            arr[idx], arr[mx] = arr[mx], arr[idx]

            for i in range(n):
                if i != idx and (arr[i] & (1 << bit)):
                    arr[i] ^= arr[idx]

            idx += 1
            if idx == n:
                break

        ans = 0
        for x in arr:
            ans = max(ans, ans ^ x)

        return ans