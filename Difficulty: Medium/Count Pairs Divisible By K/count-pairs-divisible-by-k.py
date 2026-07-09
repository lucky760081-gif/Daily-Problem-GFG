class Solution:
    def countKdivPairs(self, arr, k):
        # code here
        freq = [0] * k
        ans = 0

        for x in arr:
            r = x % k
            ans += freq[(k - r) % k]
            freq[r] += 1

        return ans