"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""

from collections import deque, Counter
class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            n1 = len(q1)
            n2 = len(q2)

            if n1 != n2:
                return False

            values1 = []
            values2 = []

            for _ in range(n1):
                node = q1.popleft()
                values1.append(node.data)

                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)

            for _ in range(n2):
                node = q2.popleft()
                values2.append(node.data)

                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            if Counter(values1) != Counter(values2):
                return False

        return not q1 and not q2        