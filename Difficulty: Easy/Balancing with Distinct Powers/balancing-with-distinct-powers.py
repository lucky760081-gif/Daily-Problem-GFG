class Solution:
    def balancePan(self, a, b):
        # code here
        while b > 0:
            remainder = b % a

            if remainder == 0:
                b //= a
            elif remainder == 1:
                b = (b - 1) // a
            elif remainder == a - 1:
                b = (b + 1) // a
            else:
                return False

        return True        
