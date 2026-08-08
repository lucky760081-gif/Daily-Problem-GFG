class Solution:
    def minEdgesReq(self, n, edges):
        # code here
        if len(edges) < n - 1:
            return -1

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        for u, v in edges:
            union(u, v)

        components = len({find(i) for i in range(n)})

        return components - 1