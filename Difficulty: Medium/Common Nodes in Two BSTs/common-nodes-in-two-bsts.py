''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        # code here
        s = set()
        ans = []

        def inorder(root):
            if root:
                inorder(root.left)
                s.add(root.data)
                inorder(root.right)

        inorder(r1)

        def check(root):
            if root:
                check(root.left)

                if root.data in s:
                    ans.append(root.data)

                check(root.right)

        check(r2)

        return ans