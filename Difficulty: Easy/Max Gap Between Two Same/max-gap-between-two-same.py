class Solution:

    def maxCharGap(self, s: str) -> int:
        # code here
        first = {}
        ans = -1

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            else:
                ans = max(ans, i - first[ch] - 1)

        return ans
        pass
