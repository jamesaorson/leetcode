import os

from models import ListNode
from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    # 342 + 465 = 807
    assert Solution().addTwoNumbers(
        ListNode.of([2, 4, 3]),
        ListNode.of([5, 6, 4]),
    ).toList() == [7, 0, 8]
    assert Solution().addTwoNumbers(
        ListNode.of([0]),
        ListNode.of([0]),
    ).toList() == [0]
    assert Solution().addTwoNumbers(
        ListNode.of([9, 9, 9, 9, 9, 9, 9]),
        ListNode.of([9, 9, 9, 9]),
    ).toList() == [8, 9, 9, 9, 0, 0, 0, 1]
    print(f"[Problem {PROBLEM}] PASS")
