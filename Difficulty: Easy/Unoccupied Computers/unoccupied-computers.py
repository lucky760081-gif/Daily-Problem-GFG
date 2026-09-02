class Solution:
    def solve(self, n, s):
        # code here
        seen = set()
        rejected = set()
        used = 0
        ans = 0

        for ch in s:
            if ch not in seen:
                seen.add(ch)

                if used < n:
                    used += 1
                else:
                    rejected.add(ch)
                    ans += 1
            else:
                if ch not in rejected:
                    used -= 1

        return ans