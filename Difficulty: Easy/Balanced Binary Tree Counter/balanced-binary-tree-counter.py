class Solution:
    def countBT(self, h: int) -> int:
        # code here
        MOD = 10**9 + 7

        if h == 0:
            return 1
        if h == 1:
            return 1

        a, b = 1, 1

        for _ in range(2, h + 1):
            c = (b * b + 2 * b * a) % MOD
            a, b = b, c

        return b        