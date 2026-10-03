class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        # code here
        m = 8 * n * n
        coil1 = [0] * m
        coil1[0] = 8 * n * n + 2 * n
        curr = coil1[0]
        flag = 1
        step = 2
        index = 1
        while index < m:
            for i in range(step):
                if index >= m:
                    break
                curr = curr - 4 * n * flag
                coil1[index] = curr
                index += 1
            for i in range(step):
                if index >= m:
                    break
                curr = curr + flag
                coil1[index] = curr
                index += 1
            flag *= -1
            step += 2
        coil2 = [16 * n * n + 1 - x for x in coil1]
        coil1.reverse()
        coil2.reverse()
        return [coil2, coil1]