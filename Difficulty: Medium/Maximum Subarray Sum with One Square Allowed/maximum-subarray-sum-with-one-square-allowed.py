class Solution: 
    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        no_square = arr[0]
        one_square = arr[0] * arr[0]
        ans = max(no_square, one_square)

        for x in arr[1:]:
            new_one = max(one_square + x, max(0, no_square) + x * x)
            new_no = max(x, no_square + x)

            no_square = new_no
            one_square = new_one
            ans = max(ans, no_square, one_square)

        return ans