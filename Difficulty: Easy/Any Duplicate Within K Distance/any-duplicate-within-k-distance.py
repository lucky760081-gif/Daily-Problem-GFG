class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        # code here
        mpp = {}

        for i in range(len(arr)):
            if arr[i] in mpp:
                if i - mpp[arr[i]] <= k:
                    return True

            mpp[arr[i]] = i

        return False        