class Solution:
    def find(self, arr):
        # code here
        need = 0
        for x in reversed(arr):
            need = (need + x + 1) // 2
        return max(1, need)