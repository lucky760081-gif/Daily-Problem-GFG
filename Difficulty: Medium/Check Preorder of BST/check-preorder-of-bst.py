class Solution:
    def canRepresentBST(self, arr):
        # code here
        stack = []
        root = float('-inf')

        for x in arr:
            if x < root:
                return False

            while stack and stack[-1] < x:
                root = stack.pop()

            stack.append(x)

        return True