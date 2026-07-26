class Solution:
    def levelSort(self, arr):
        # code here
        ans = []
        i = 0
        level = 1
        n = len(arr)

        while i < n:
            ans.append(sorted(arr[i:min(i + level, n)]))
            i += level
            level <<= 1

        return ans