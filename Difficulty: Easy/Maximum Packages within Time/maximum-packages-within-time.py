class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        k = min(totalTime, len(arr))
        window = sum(arr[:k])
        ans = window

        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            ans = max(ans, window)

        return ans        