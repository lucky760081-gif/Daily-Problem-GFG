class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        # code here
        n = len(arr) // 2
        a = sorted(arr[:n])
        b = sorted(arr[n:])

        j = 0
        ans = 0

        for x in a:
            while j < n and x >= 5 * b[j]:
                j += 1
            ans += j

        return ans