class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # code here
        lengths = [len(s)]
        i = 1

        while lengths[-1] < pos:
            lengths.append(2 * lengths[-1] + i)
            i += 1

        for j in range(len(lengths) - 1, 0, -1):
            prev = lengths[j - 1]
            step = j

            if pos <= prev:
                continue
            elif pos <= prev + step:
                return '$'
            else:
                pos = 2 * prev + step - pos + 1

        return s[pos - 1]