class Solution:
    def maximumWeight(self, n, edges, queries):
        # code here
        edges.sort(key=lambda x: x[2])
        indexed = sorted((x, i) for i, x in enumerate(queries))

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ans = [0] * len(queries)
        total = 0
        j = 0

        for x, idx in indexed:
            while j < len(edges) and edges[j][2] <= x:
                u, v, w = edges[j]
                ru = find(u)
                rv = find(v)

                if ru != rv:
                    total += size[ru] * size[rv]

                    if size[ru] < size[rv]:
                        ru, rv = rv, ru

                    parent[rv] = ru
                    size[ru] += size[rv]

                j += 1

            ans[idx] = total

        return ans