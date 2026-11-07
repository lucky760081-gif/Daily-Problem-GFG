class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        # code here
        reserved = set(arr)
        used = set()
        next_suffix = {}
        ans = []

        for name in arr:
            if name not in used:
                used.add(name)
                ans.append(name)
            else:
                k = next_suffix.get(name, 1)

                while name + str(k) in reserved or name + str(k) in used:
                    k += 1

                new_name = name + str(k)
                ans.append(new_name)
                used.add(new_name)
                next_suffix[name] = k + 1

        return ans        