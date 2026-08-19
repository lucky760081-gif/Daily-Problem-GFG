class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        arr.sort()
        n = len(arr)

        def count_leq(target):
            ans = 0

            for i in range(n - 2):
                left = i + 1
                right = n - 1

                while left < right:
                    total = arr[i] + arr[left] + arr[right]

                    if total <= target:
                        ans += right - left
                        left += 1
                    else:
                        right -= 1

            return ans

        return count_leq(r) - count_leq(l - 1)