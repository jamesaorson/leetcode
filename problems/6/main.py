import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert (
        Solution().convert(
            "AB",
            1,
        ) == "AB"
    )
    assert (
        Solution().convert(
            "PAYPALISHIRING",
            3,
        ) == "PAHNAPLSIIGYIR"
    )
    assert (
        Solution().convert(
            "PAYPALISHIRING",
            4,
        ) == "PINALSIGYAHRPI"
    )
    assert (
        Solution().convert(
            "A",
            1,
        ) == "A"
    )
    print(f"[Problem {PROBLEM}] PASS")
