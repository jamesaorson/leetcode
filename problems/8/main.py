import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert (
        Solution().myAtoi(
            "21474836460",
        ) == 2147483647
    )
    assert (
        Solution().myAtoi(
            "-91283472332"
        ) == -2147483648
    )
    assert (
        Solution().myAtoi(
            "42",
        ) == 42
    )
    assert (
        Solution().myAtoi(
            "-042",
        ) == -42
    )
    assert (
        Solution().myAtoi(
            "1337c0d3"
        ) == 1337
    )
    assert (
        Solution().myAtoi(
            "0-1"
        ) == 0
    )
    assert (
        Solution().myAtoi(
            "words and 987"
        ) == 0
    )
    print(f"[Problem {PROBLEM}] PASS")
