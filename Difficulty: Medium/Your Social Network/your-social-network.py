class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr) + 1
        parent = [0] * (n + 1)

        for i in range(2, n + 1):
            parent[i] = arr[i - 2]

        ans = []

        for i in range(2, n + 1):
            cur = i
            dist = 0
            path = []

            while parent[cur] != 0:
                cur = parent[cur]
                dist += 1
                path.append([cur, dist])

            for j, k in reversed(path):
                ans.append([i, j, k])

        return ans