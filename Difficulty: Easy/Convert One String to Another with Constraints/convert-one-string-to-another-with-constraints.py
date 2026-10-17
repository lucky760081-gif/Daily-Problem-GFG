class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # code here
        if len(s1) != len(s2):
            return False

        a = [(c, i) for i, c in enumerate(s1) if c != '#']
        b = [(c, i) for i, c in enumerate(s2) if c != '#']

        if len(a) != len(b):
            return False

        for (c1, i), (c2, j) in zip(a, b):
            if c1 != c2:
                return False
            if c1 == 'A' and j > i:
                return False
            if c1 == 'B' and j < i:
                return False

        return True
