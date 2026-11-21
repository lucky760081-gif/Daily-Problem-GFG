class Solution:
    def smallestSubWithSum(self, arr, x):
        # code here 
        left = 0
        total = 0
        ans = float('inf')

        for right in range(len(arr)):
            total += arr[right]

            while total > x:
                ans = min(ans, right - left + 1)
                total -= arr[left]
                left += 1

        return ans if ans != float('inf') else 0        