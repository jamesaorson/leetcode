class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        max_len = 0
        for c in s:
            while c in chars:
                max_len = max(len(chars), max_len)
                chars = chars[1:]
            chars.append(c)
        result = max(len(chars), max_len)
        return result
