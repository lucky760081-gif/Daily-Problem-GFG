class Solution:
    def goodIndices(self, arr):
        # code here
        n = len(arr)
        state = [0] * n
        ans = 0

        for i in range(n):
            if state[i] != 0:
                continue

            path = []
            pos = i

            while 0 <= pos < n and state[pos] == 0:
                state[pos] = 1
                path.append(pos)
                pos += arr[pos]

            if pos < 0 or pos >= n:
                good = True
            elif state[pos] == 2:
                good = True
            else:
                good = False

            for j in reversed(path):
                state[j] = 2 if good else 3
                if good:
                    ans += 1

        return ans
