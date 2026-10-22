# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res: dict[str: list[str]] = {}
        for i in range(len(strs)):
            tmp = "".join(sorted(strs[i]))
            if tmp in res.keys():
                res[tmp].append(strs[i])
            else:
                res[tmp] = [strs[i]]

        return list(res.values())
        