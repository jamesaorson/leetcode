import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert Solution().intToRoman(3749) == "MMMDCCXLIX"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"
    print(f"[Problem {PROBLEM}] PASS")
