class Solution:

    def maxValue(self, n: int) -> int:
        """code here"""
        while n & (n >> 1) & (n >> 2):
            n &= ~(1 << ((n & (n >> 1) & (n >> 2)).bit_length() - 1))
        return n
