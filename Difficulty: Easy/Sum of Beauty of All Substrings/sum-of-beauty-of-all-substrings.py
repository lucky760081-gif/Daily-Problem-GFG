class Solution:
    def beautySum(self, s: str) -> int:
        # code here
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            mx = 0
            for j in range(i, n):
                idx = ord(s[j]) - 97
                freq[idx] += 1
                mx = max(mx, freq[idx])

                mn = n
                for f in freq:
                    if f and f < mn:
                        mn = f

                ans += mx - mn

        return ans