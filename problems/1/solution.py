class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        for i in range(len(nums) - 1):
            elem = nums[i]
            to_find = target - elem
            for j in range(i + 1, len(nums)):
                if nums[j] == to_find:
                    return [i, j]
        return None

