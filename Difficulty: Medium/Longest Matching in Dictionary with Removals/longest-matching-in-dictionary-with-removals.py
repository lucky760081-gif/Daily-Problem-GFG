class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # code here
        pos = [[] for _ in range(26)]

        for i, ch in enumerate(s):
            pos[ord(ch) - 97].append(i)

        ans = ""

        for word in d:
            prev = -1
            ok = True

            for ch in word:
                arr = pos[ord(ch) - 97]

                lo = 0
                hi = len(arr)

                while lo < hi:
                    mid = (lo + hi) // 2
                    if arr[mid] <= prev:
                        lo = mid + 1
                    else:
                        hi = mid

                if lo == len(arr):
                    ok = False
                    break

                prev = arr[lo]

            if ok and (len(word) > len(ans) or
                       (len(word) == len(ans) and word < ans)):
                ans = word

        return ans        