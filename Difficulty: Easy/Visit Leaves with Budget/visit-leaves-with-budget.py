''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        # code here
        costs = []
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()

            if node is None:
                continue

            if node.left is None and node.right is None:
                costs.append(level)
            else:
                if node.left:
                    stack.append((node.left, level + 1))
                if node.right:
                    stack.append((node.right, level + 1))

        costs.sort()

        total = 0
        count = 0

        for cost in costs:
            if total + cost > k:
                break
            total += cost
            count += 1

        return count        