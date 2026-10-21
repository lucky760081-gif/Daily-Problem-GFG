class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        curr = ans = arr[0]

        for x in arr[1:]:
            curr = min(x, curr + x)
            ans = min(ans, curr)

        return ans
