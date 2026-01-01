import os

from solution import Solution

PROBLEM = os.path.basename(__file__)


if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert (
        Solution().isPalindrome(
            1001,
        )
    )
    assert (
        Solution().isPalindrome(
            121,
        )
    )
    assert (
        not Solution().isPalindrome(
            -121,
        )
    )
    assert (
        not Solution().isPalindrome(
            10,
        )
    )
    
    assert (
        Solution().isPalindrome(
            0,
        )
    )
    print(f"[Problem {PROBLEM}] PASS")
