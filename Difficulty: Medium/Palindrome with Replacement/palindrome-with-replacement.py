class Solution:
    def minimumSum(self, s: str) -> int:
        # code here
        n = len(s)
        fixed = []

        for i in range(n // 2):
            a, b = s[i], s[n - 1 - i]

            if a != '?' and b != '?' and a != b:
                return -1

            if a != '?':
                fixed.append(ord(a))
            elif b != '?':
                fixed.append(ord(b))

        if n % 2:
            if s[n // 2] != '?':
                fixed.append(ord(s[n // 2]))

        return 2 * sum(abs(fixed[i] - fixed[i - 1]) for i in range(1, len(fixed)))