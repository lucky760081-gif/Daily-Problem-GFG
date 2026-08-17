class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        N = n * n
    
        jump = [0] * (N + 1)
    
        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]
    
        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]
    
        from collections import deque
    
        q = deque([(1, 0)])
        visited = [False] * (N + 1)
        visited[1] = True
    
        while q:
            pos, throws = q.popleft()
    
            if pos == N:
                return throws
    
            for dice in range(1, 7):
                nxt = pos + dice
    
                if nxt > N:
                    break
    
                if jump[nxt] != 0:
                    nxt = jump[nxt]
    
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, throws + 1))
    
        return -1