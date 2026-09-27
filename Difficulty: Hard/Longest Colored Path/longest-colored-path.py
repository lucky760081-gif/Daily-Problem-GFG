class Solution:
    def longestPath(self, s, edges):
        # code here
        n = len(s)
        g = [[] for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        order = [0]

        for u in order:
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                order.append(v)

        down = [1] * n

        for u in reversed(order):
            best = 0
            for v in g[u]:
                if parent[v] == u and s[v] == s[u]:
                    best = max(best, down[v])
            down[u] = 1 + best

        up = [1] * n
        best_same = [0] * n
        ans = 1

        for u in order:
            first = 0
            second = 0

            if parent[u] != -1 and s[parent[u]] == s[u]:
                val = up[u]
                if val > first:
                    second = first
                    first = val
                elif val > second:
                    second = val

            for v in g[u]:
                if parent[v] == u and s[v] == s[u]:
                    val = down[v]
                    if val > first:
                        second = first
                        first = val
                    elif val > second:
                        second = val

            best_same[u] = first
            ans = max(ans, 1 + first + second)

            for v in g[u]:
                if parent[v] == u:
                    if s[v] == s[u]:
                        other = first

                        if down[v] == first:
                            other = second

                        up[v] = 1 + other
                    else:
                        up[v] = 1

        for u, v in edges:
            u -= 1
            v -= 1

            if s[u] != s[v]:
                ans = max(ans, 2 + best_same[u] + best_same[v])

        return ans