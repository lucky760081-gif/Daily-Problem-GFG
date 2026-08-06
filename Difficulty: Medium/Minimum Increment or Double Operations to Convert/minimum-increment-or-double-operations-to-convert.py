class Solution:
    def countMinOperations(self, arr):
        # code here
        inc = 0
        max_bits = 0

        for x in arr:
            inc += bin(x).count('1')
            if x > 0:
                max_bits = max(max_bits, x.bit_length() - 1)

        return inc + max_bits