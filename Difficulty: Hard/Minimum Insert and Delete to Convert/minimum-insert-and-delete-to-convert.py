class Solution:
    def minInsAndDel(self, a, b):
        # code here
        pos = {x: i for i, x in enumerate(b)}
        
        arr = [pos[x] for x in a if x in pos]
        
        lis = []
        from bisect import bisect_left
        
        for x in arr:
            idx = bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
        
        lcs = len(lis)
        return (len(a) - lcs) + (len(b) - lcs)