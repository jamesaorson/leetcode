# TODO: Fix
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        start = 0
        result = ""
        while start < s_len:
            end = s_len - 1
            while end >= start:
                s_temp = s[start:end + 1]
                if self.is_palindrome(s_temp):
                    result = s_temp if len(s_temp) > len(result) else result
                end -= 1
            start += 1
        return result


    def is_palindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

