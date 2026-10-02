class Solution:
    def lexiString(self, s: str) -> str:
        # code here
        s = s + s
        n = len(s) // 2
        i = 0
        j = 1
        k = 0

        while i < n and j < n and k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                i = i + k + 1
                if i <= j:
                    i = j + 1
                k = 0
            else:
                j = j + k + 1
                if j <= i:
                    j = i + 1
                k = 0

        start = min(i, j)
        return s[start:start + n]