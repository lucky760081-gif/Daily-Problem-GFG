class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # code here
        def count_at_most(x):
            if x < 0:
                return 0

            left = 0
            curr = 0
            cnt = 0

            for right in range(len(arr)):
                curr += arr[right]

                while curr > x:
                    curr -= arr[left]
                    left += 1

                cnt += right - left + 1

            return cnt

        return count_at_most(r) - count_at_most(l - 1)