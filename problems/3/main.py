import os
import sys

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert Solution().lengthOfLongestSubstring(
        "abcabcbb"
    ) == 3
    assert Solution().lengthOfLongestSubstring(
        "bbbbb"
    ) == 1
    assert Solution().lengthOfLongestSubstring(
        "pwwkew"
    ) == 3
    print(f"[Problem {PROBLEM}] PASS")
