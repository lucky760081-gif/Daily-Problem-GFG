class Solution:

    def getMarks(self, l, r, rank):
        """code here"""
        prefix = []
        total = 0

        for i in range(len(l)):
            total += r[i] - l[i] + 1
            prefix.append(total)

        ans = []

        for k in rank:
            low, high = 0, len(prefix) - 1

            while low < high:
                mid = (low + high) // 2

                if prefix[mid] >= k:
                    high = mid
                else:
                    low = mid + 1

            i = low
            prev = prefix[i - 1] if i > 0 else 0
            ans.append(l[i] + k - prev - 1)

        return ans