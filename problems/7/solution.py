import math

class Solution:
    MAX = (2**31) - 1
    MIN = -(2**31)

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = 1 if x >= 0 else -1
        x *= sign # negate the sign, if it exists
        modulo = 10
        place = 10**(math.floor(math.log10(x)))
        result = 0
        while x > 0:
            step = x % modulo
            result += (step * place)
            x //= 10
            place /= 10
        result = result * sign
        if result > Solution.MAX or result < Solution.MIN:
            return 0
        return int(result)