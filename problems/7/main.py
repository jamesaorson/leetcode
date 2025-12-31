import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert (
        Solution().reverse(
            123,
        ) == 321
    )
    assert (
        Solution().reverse(
            -123,
        ) == -321
    )
    assert (
        Solution().reverse(
            120
        ) == 21
    )
    print(f"[Problem {PROBLEM}] PASS")
