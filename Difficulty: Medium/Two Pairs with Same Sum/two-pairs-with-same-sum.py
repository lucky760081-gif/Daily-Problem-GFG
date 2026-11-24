class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        # code here
        n = len(arr)
        seen = {}
        ans = None

        for i in range(n):
            for j in range(i + 1, n):
                total = arr[i] + arr[j]

                if total in seen:
                    for a, b in seen[total]:
                        if a != i and a != j and b != i and b != j:
                            candidate = (a, b, i, j)

                            if ans is None or candidate < ans:
                                ans = candidate
                            break

                else:
                    seen[total] = []

                seen[total].append((i, j))

        return list(ans) if ans else [-1, -1, -1, -1]