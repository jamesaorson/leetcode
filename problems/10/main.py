import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert (
        not Solution().isMatch(
            "aa",
            "a"
        )
    )
    assert (
        Solution().isMatch(
            "aa",
            "a*"
        )
    )
    assert (
        Solution().isMatch(
            "ab",
            ".*",
        )
    )
    print(f"[Problem {PROBLEM}] PASS")
