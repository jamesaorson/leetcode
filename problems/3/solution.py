class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        curr_len = 0
        max_len = 0
        for c in s:
            if c in chars:
                max_len = max(curr_len, max_len)
                curr_len = 1
                chars = {c}
                continue
            chars.add(c)
            curr_len += 1
        result = max(curr_len, max_len)
        return result
