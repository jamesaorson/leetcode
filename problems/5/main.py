import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert (
        Solution().longestPalindrome(
            "babad",
        ) in ["bab", "aba"]
    )
    assert (
        Solution().longestPalindrome(
            "cbbd",
        ) == "bb"
    )
    print(f"[Problem {PROBLEM}] PASS")
