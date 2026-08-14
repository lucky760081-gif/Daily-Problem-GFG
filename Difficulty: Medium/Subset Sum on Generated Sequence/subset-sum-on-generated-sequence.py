class Solution:
    def isPossible(self, arr, s, x):
        # code here 
        if x == 0:
            return True

        nums = []
        pref = s

        if s <= x:
            nums.append(s)

        for v in arr:
            cur = pref + v

            if cur <= x:
                nums.append(cur)
            else:
                break

            pref += cur

        for num in reversed(nums):
            if num <= x:
                x -= num

        return x == 0