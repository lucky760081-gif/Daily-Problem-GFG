class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        MOD = 1000000007

        fact = 1
        for i in range(1, 2 * n + 1):
            fact = fact * i % MOD

        inv_fact_n = pow(
            __import__('math').prod(range(1, n + 1)),
            MOD - 2,
            MOD
        )

        inv_fact_n1 = pow(
            __import__('math').prod(range(1, n + 1)),
            MOD - 2,
            MOD
        )

        comb = fact
        comb = comb * inv_fact_n % MOD
        comb = comb * inv_fact_n % MOD

        return comb * pow(n + 1, MOD - 2, MOD) % MOD