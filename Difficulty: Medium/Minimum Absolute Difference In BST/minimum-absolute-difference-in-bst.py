'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        # code here
        stack = []
        curr = root
        prev = None
        ans = float('inf')

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev is not None:
                ans = min(ans, curr.data - prev)

            prev = curr.data
            curr = curr.right

        return ans        