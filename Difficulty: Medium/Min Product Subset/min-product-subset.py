class Solution:
    def minProd(self, arr):
        # code here
        neg = []
        pos = []
        zero = 0

        for x in arr:
            if x < 0:
                neg.append(x)
            elif x > 0:
                pos.append(x)
            else:
                zero += 1

        if len(neg) == 0:
            if zero:
                return 0
            return min(pos)

        if len(neg) % 2 == 0:
            neg.remove(max(neg))

        ans = 1

        for x in neg:
            ans *= x

        for x in pos:
            ans *= x

        return ans