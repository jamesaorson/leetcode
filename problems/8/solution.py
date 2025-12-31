# TODO: Fix
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s = s.strip()
        sign = 1 if s[0] != '-' else -1
        result = 0
        if s[0] in ['-', '+']:
            s = s[1:]
        nums = []
        for c in s:
            if not c.isnumeric():
                break
            if c == '0':
                continue
            x = ord(c) - ord('0')
            nums.append(x)
        place = 10 ** (len(nums) - 1)
        for num in nums:
            result += num * place
            place //= 10
        return sign * result