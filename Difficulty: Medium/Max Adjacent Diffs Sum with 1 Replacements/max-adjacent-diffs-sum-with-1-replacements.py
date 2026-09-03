class Solution:
    def maxDiffSum(self, arr):
        # code here
        orig = 0
        one = 0

        for i in range(1, len(arr)):
            x = arr[i]
            prev = arr[i - 1]

            n_orig = max(
                orig + abs(prev - x),
                one + abs(1 - x)
            )

            n_one = max(
                orig + abs(prev - 1),
                one
            )

            orig, one = n_orig, n_one

        return max(orig, one)