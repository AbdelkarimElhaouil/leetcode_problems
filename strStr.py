# 28. Find the Index of the First Occurrence in a String

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
                    j = lps[j - 1]

            return lps
        lps, i, j = build_lps(), 0, 0
        while i < txt_len:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]

            if j == patt_len:
                return i - j
        return -1