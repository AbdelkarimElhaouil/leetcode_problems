# 28. Find the Index of the First Occurrence in a String

# still working on it

def build_lps(pattern: str):
    lps = [0]
    j, i, patt_len = 0, 1, len(pattern)
    while patt_len > i:
        if pattern[j] == pattern[i]:
            lps.append(j+1)
            j += 1
            i += 1
        elif j == 0:
            lps.append(0)
            i += 1
        else:
            j = 0
            
    return lps
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        patt_len, txt_len = len(needle), len(haystack)
        def build_lps():
            lps = [0]
            i, j = 1, 0
            while i < patt_len:
                if needle[i] == needle[j]:
                    lps.append(j + 1)
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                    lps.append(0)
                else:
                    j = 0

            return lps
        lps, i, j = build_lps(), 0, 0
        print(patt_len, lps)
        while i < txt_len:
            if needle[j] == haystack[i]:
                print(needle[:j])
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                print(needle[:j], j)
                j = lps[j - 1]

            if j == patt_len:
                return i - j
        return -1

s = Solution()

print(s.strStr("aabaaabaaac", "aabaaac"))
# print(s.strStr("sadbutsad", "sad"))
# print(s.strStr("sadbutsas", "sad"))
# print(build_lps("aabaaac"))