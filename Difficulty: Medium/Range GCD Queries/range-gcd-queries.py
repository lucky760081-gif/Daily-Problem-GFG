class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # code here
        n = len(arr)
        size = 1

        while size < n:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(n):
            tree[size + i] = arr[i]

        for i in range(size - 1, 0, -1):
            tree[i] = gcd(tree[2 * i], tree[2 * i + 1])

        def update(index, value):
            p = size + index
            tree[p] = value

            p //= 2
            while p:
                tree[p] = gcd(tree[2 * p], tree[2 * p + 1])
                p //= 2

        def query(left, right):
            left += size
            right += size

            ans = 0

            while left <= right:
                if left & 1:
                    ans = gcd(ans, tree[left])
                    left += 1

                if not (right & 1):
                    ans = gcd(ans, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return ans

        result = []

        for query_data in queries:
            if query_data[0] == 0:
                result.append(query(query_data[1], query_data[2]))
            else:
                update(query_data[1], query_data[2])

        return result        