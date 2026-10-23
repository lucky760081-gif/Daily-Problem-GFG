''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        # code here
        arr = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            arr.append(node.data)
            node = node.right

        def merge_sort(a):
            if len(a) <= 1:
                return a, 0

            mid = len(a) // 2
            left, x = merge_sort(a[:mid])
            right, y = merge_sort(a[mid:])
            merged = []
            i = j = 0
            count = x + y

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += len(left) - i
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, count

        return merge_sort(arr)[1]