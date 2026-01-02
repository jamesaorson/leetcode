class Solution:
    def maxArea(self, height: list[int]) -> int:
        num_heights = len(height)
        max_area = 0
        i = 0
        j = num_heights - 1
        while i < j:
            left, right = height[i], height[j]
            area = min(left, right) * (j - i)
            max_area = area if area > max_area else max_area
            if left > right:
                j -= 1
            else:
                i += 1
        return max_area
