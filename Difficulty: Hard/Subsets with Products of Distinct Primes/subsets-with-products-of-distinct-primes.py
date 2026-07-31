class Solution:
    def countSubsets(self, arr):
        # code here
        MOD = 1000000007

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        freq = [0] * 31
        for x in arr:
            freq[x] += 1

        masks = [0] * 31

        for x in range(2, 31):
            t = x
            mask = 0
            ok = True

            for i, p in enumerate(primes):
                cnt = 0
                while t % p == 0:
                    cnt += 1
                    t //= p

                if cnt > 1:
                    ok = False
                    break

                if cnt == 1:
                    mask |= (1 << i)

            if ok:
                masks[x] = mask

        dp = [0] * 1024
        dp[0] = 1

        for x in range(2, 31):
            if freq[x] == 0 or masks[x] == 0:
                continue

            m = masks[x]

            for mask in range(1023, -1, -1):
                if (mask & m) == 0:
                    dp[mask | m] = (dp[mask | m] + dp[mask] * freq[x]) % MOD

        ans = (sum(dp) - 1) % MOD

        ans = ans * pow(2, freq[1], MOD) % MOD

        return ans