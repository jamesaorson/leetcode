class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_index = 0
        prev_c = ''
        for c in p:
            if s_index >= len(s):
                return False
            if c == '.':
                s_index += 1
            elif c == '*':
                while s_index < len(s):
                    if prev_c == '.' or s[s_index] == prev_c:
                        s_index += 1
            elif c == s[s_index]:
                s_index += 1
            else:
                return False
            prev_c = c
        return s_index == len(s)