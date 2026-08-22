''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        # code here
        def find_path(node, target, path):
            if not node:
                return False

            path.append(node)

            if node.data == target:
                return True

            if find_path(node.left, target, path) or find_path(node.right, target, path):
                return True

            path.pop()
            return False

        path_p = []
        path_q = []

        find_path(root, p, path_p)
        find_path(root, q, path_q)

        # Find first common node (LCA)
        i = 0
        while i < min(len(path_p), len(path_q)) and path_p[i] == path_q[i]:
            i += 1

        lca_index = i - 1

        # Path from p to LCA and LCA to q
        directions = []

        # p -> LCA
        for j in range(len(path_p) - 1, lca_index, -1):
            parent = path_p[j - 1]
            child = path_p[j]

            if parent.left == child:
                directions.append('L')
            else:
                directions.append('R')

        # LCA -> q
        for j in range(lca_index + 1, len(path_q)):
            parent = path_q[j - 1]
            child = path_q[j]

            if parent.left == child:
                directions.append('L')
            else:
                directions.append('R')

        # No direction change means no turns
        if len(directions) <= 1:
            return -1

        turns = 0
        for i in range(1, len(directions)):
            if directions[i] != directions[i - 1]:
                turns += 1

        return turns if turns > 0 else -1