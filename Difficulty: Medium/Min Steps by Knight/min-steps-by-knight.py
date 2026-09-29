class Solution:
	def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
		#Code here
        sx, sy = knightPos[0] - 1, knightPos[1] - 1
        tx, ty = targetPos[0] - 1, targetPos[1] - 1

        if sx == tx and sy == ty:
            return 0

        moves = (
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        )

        q1 = deque([(sx, sy)])
        q2 = deque([(tx, ty)])

        d1 = {(sx, sy): 0}
        d2 = {(tx, ty): 0}

        while q1 and q2:
            if len(q1) <= len(q2):
                for _ in range(len(q1)):
                    x, y = q1.popleft()

                    for dx, dy in moves:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n:
                            if (nx, ny) in d2:
                                return d1[(x, y)] + 1 + d2[(nx, ny)]

                            if (nx, ny) not in d1:
                                d1[(nx, ny)] = d1[(x, y)] + 1
                                q1.append((nx, ny))
            else:
                for _ in range(len(q2)):
                    x, y = q2.popleft()

                    for dx, dy in moves:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n:
                            if (nx, ny) in d1:
                                return d2[(x, y)] + 1 + d1[(nx, ny)]

                            if (nx, ny) not in d2:
                                d2[(nx, ny)] = d2[(x, y)] + 1
                                q2.append((nx, ny))

        return -1