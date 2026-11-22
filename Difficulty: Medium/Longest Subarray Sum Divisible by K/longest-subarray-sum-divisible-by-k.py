class Solution:
	def longestSubarrayDivK(self, arr, k):
		# code here
        mpp = {0: -1}
        total = 0
        ans = 0

        for i, num in enumerate(arr):
            total = (total + num) % k

            if total in mpp:
                ans = max(ans, i - mpp[total])
            else:
                mpp[total] = i

        return ans		