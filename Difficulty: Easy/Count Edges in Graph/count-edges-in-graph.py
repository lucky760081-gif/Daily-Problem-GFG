class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # code here
        return sum(len(neighbors) for neighbors in adj) // 2