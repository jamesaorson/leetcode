class Solution:
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1 if s[0] != '-' else -1
        result = 0
        if s[0] in ['-', '+', '0']:
            s = s[1:]
        nums = []
        for c in s:
            if not c.isnumeric():
                break
            x = ord(c) - ord('0')
            nums.append(x)
        place = 10 ** (len(nums) - 1)
        for num in nums:
            result += num * place
            place //= 10
        result *= sign
        return max(
            min(
                result,
                Solution.MAX
            ),
            Solution.MIN
        )
