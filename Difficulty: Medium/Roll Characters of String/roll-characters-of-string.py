class Solution:
    def findRollOut(self, s, roll):
        # code here
        n = len(s)
        total = 0
        rolls = [0] * n

        for i in range(len(roll) - 1, -1, -1):
            total = (total + 1) % 26
            rolls[roll[i] - 1] = (rolls[roll[i] - 1] + 1) % 26

        total = 0
        for i in range(n - 1, -1, -1):
            total = (total + rolls[i]) % 26
            rolls[i] = total

        ans = []
        for i in range(n):
            shift = rolls[i]
            ans.append(chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a')))

        return ''.join(ans)