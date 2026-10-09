class Solution:
    def minOperation(self, n):
        # code here
        operations = 0

        while n > 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 1

            operations += 1

        return operations        