import os

from solution import Solution

PROBLEM = os.path.basename(__file__)

if __name__ == "__main__":
    print(f"[Problem {PROBLEM}] START")
    assert Solution().twoSum(
        [2, 7, 11, 15],
        9,
    ) == [0, 1]
    assert Solution().twoSum(
        [3, 2, 4],
        6,
    ) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    print(f"[Problem {PROBLEM}] PASS")
