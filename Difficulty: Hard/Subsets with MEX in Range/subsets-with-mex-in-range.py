class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        """ code here """
        MOD = 10**9 + 7
        n = len(arr)

        freq = [0] * (n + 2)
        for x in arr:
            freq[x] += 1

        ans = 0
        prod = 1
        prefix = 0

        for mex in range(r + 1):
            greater = n - prefix - freq[mex]

            if l <= mex:
                ans = (ans + prod * pow(2, greater, MOD)) % MOD

            prod = prod * (pow(2, freq[mex], MOD) - 1) % MOD
            prefix += freq[mex]

        return ans        