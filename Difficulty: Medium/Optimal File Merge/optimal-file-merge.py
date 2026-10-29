class Solution:
    def minComputation(self, files):
        # code here
        heapq.heapify(files)
        ans = 0

        while len(files) > 1:
            x = heapq.heappop(files)
            y = heapq.heappop(files)
            cost = x + y
            ans += cost
            heapq.heappush(files, cost)

        return ans        