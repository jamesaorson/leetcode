from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Used later to determine if we need an additional index to calculate the median or not
        left_len = len(nums1)
        right_len = len(nums2)
        total_len = left_len + right_len
        # Discards the floating point portion
        median_index = total_len // 2
        # indices for each list
        left = 0 # nums1
        right = 0 # nums2
        i = 0 # actual index for "total list of nums"
        median = 0.0
        prev_number = 0.0
        while i <= median_index:
            prev_number = median
            if left >= left_len:
                median = nums2[right]
                right += 1
            elif right >= right_len:
                median = nums1[left]
                left += 1
            elif nums1[left] > nums2[right]:
                median = nums2[right]
                right += 1
            else:
                median = nums1[left]
                left += 1
            i += 1
        if total_len % 2 == 0:
            median = (prev_number + median) / 2.0
        return median