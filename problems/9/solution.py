import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        start_place = 10 ** math.floor(math.log10(x))
        end_place = 10
        while start_place >= end_place:
            if x // start_place != x % end_place:
                return False
            start_place /= 10
            end_place *= 10
        return True