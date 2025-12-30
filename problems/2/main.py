import os
import sys

from models import ListNode
from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    try:
        assert Solution().addTwoNumbers(
            ListNode.of([2, 4, 3]),
            ListNode.of([5, 6, 4]),
        ) == [7, 0, 8]
        assert Solution().addTwoNumbers(
            ListNode.of([0]),
            ListNode.of([0]),
        ) == [0]
        assert Solution().addTwoNumbers(
            ListNode.of([9, 9, 9, 9, 9, 9, 9]),
            ListNode.of([9, 9, 9, 9]),
        ) == [8, 9, 9, 9, 0, 0, 0, 1]
    except Exception as e:
        print(f"[Problem {PROBLEM}] FAIL: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"[Problem {PROBLEM}] PASS")
