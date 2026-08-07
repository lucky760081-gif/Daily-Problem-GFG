class Solution:
    def countFriendsPairings(self, n: int) -> int:
        # code here 
        if n <= 2:
            return n

        dp1, dp2 = 1, 2

        for i in range(3, n + 1):
            dp1, dp2 = dp2, dp2 + (i - 1) * dp1

        return dp2