class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        n = len(s)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + (s[i] in "aeiou")

        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])

        return ans        