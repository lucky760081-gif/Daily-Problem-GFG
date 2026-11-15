class Solution:
    def subsequenceSum(self, s):
        """code here"""
        mod = 10**9 + 7
        ans = 0
        n = len(s)

        for ch in s:
            ans = (ans + int(ch) * pow(2, n - 1, mod)) % mod

        return ans
        