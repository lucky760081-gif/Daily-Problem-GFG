class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        # code here
        n, m = len(s1), len(s2)

        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    pre[i + 1][j + 1] = pre[i][j] + 1
                else:
                    pre[i + 1][j + 1] = max(pre[i][j + 1], pre[i + 1][j])

        suf = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    suf[i][j] = suf[i + 1][j + 1] + 1
                else:
                    suf[i][j] = max(suf[i + 1][j], suf[i][j + 1])

        lcs = pre[n][m]
        ans = 0

        for pos in range(n + 1):
            used = set()
            for j in range(m):
                if s2[j] in used:
                    continue
                if pre[pos][j] + 1 + suf[pos][j + 1] == lcs + 1:
                    ans += 1
                    used.add(s2[j])

        return ans