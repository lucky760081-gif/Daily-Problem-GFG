class Solution:
    def countSubstring(self, s):
        # code here
        n = len(s)

        pref = 0
        vals = [0]
        for ch in s:
            pref += 1 if ch == '1' else -1
            vals.append(pref)

        comp = sorted(set(vals))
        idx = {v: i + 1 for i, v in enumerate(comp)}

        bit = [0] * (len(comp) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        update(idx[0])

        pref = 0
        for ch in s:
            pref += 1 if ch == '1' else -1
            p = idx[pref]
            ans += query(p - 1)
            update(p)

        return ans