import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert (
        Solution().findMedianSortedArrays(
            [1, 3],
            [2],
        )
        == 2.0
    )
    assert (
        Solution().findMedianSortedArrays(
            [1, 2],
            [3, 4],
        )
        == 2.5
    )
    print(f"[Problem {PROBLEM}] PASS")
