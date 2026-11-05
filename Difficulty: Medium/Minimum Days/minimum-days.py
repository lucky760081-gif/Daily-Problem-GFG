class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        # code here
        n = len(s)
        pos = [0] * n

        for i, x in enumerate(p):
            pos[x] = i + 1

        ans = 0

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                ans = max(ans, min(pos[i], pos[i + 1]))

        return ans