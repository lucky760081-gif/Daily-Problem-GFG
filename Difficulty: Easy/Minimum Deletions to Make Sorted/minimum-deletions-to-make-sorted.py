class Solution:
    def minDeletions(self, arr):
        # code here
        lis = []

        for x in arr:
            left, right = 0, len(lis)
            
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            if left == len(lis):
                lis.append(x)
            else:
                lis[left] = x

        return len(arr) - len(lis)