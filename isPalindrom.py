# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st, en = 0, len(s) - 1
        while st <= en:
            if not s[st].isalnum():
                st += 1
            elif not s[en].isalnum():
                en -= 1
            elif s[en].lower() != s[st].lower():
                return False
            else:
                st += 1
                en -= 1
        return True
