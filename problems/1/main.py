import os
import sys

from solution import Solution

PROBLEM = os.path.basename(__file__)

if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    try:
        assert Solution().twoSum(
            [2, 7, 11, 15],
            9,
        ) == [0, 1]
        assert Solution().twoSum(
            [3, 2, 4],
            6,
        ) == [1, 2]
        assert Solution().twoSum([3, 3], 6) == [0, 1]
    except Exception as e:
        print(f"[Problem {PROBLEM}] FAIL: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"[Problem {PROBLEM}] PASS")
