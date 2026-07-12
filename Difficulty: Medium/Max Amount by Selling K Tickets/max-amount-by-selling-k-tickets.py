class Solution:
    def maxAmount(self, arr, k):
        # code here
        MOD = 10**9 + 7

        pq = [-x for x in arr]
        heapq.heapify(pq)

        ans = 0

        while k and pq:
            x = -heapq.heappop(pq)
            ans = (ans + x) % MOD
            k -= 1
            if x > 1:
                heapq.heappush(pq, -(x - 1))

        return ans % MOD