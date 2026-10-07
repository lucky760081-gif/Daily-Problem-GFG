'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
        # code here
        self.ans = -10**18
        self.leaves = 0

        def dfs(node):
            if not node:
                return -10**18

            if not node.left and not node.right:
                self.leaves += 1
                return node.data

            left = dfs(node.left) if node.left else -10**18
            right = dfs(node.right) if node.right else -10**18

            if node.left and node.right:
                self.ans = max(self.ans, left + node.data + right)
                return node.data + max(left, right)

            if node.left:
                return node.data + left

            return node.data + right

        dfs(root)

        if self.leaves < 2:
            return -1

        return self.ans