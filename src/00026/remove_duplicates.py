from typing import List

"""
Leetcode problem link
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Time complexity 
    O(n) as all the elements of the array are processed one linearly
    
Space complexuty
    O(1) as there is not additional space being consumed
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_idx = 1

        for curr_idx in range(1, len(nums)):
            if nums[curr_idx] != nums[curr_idx - 1]:
                nums[unique_idx] = nums[curr_idx]
                unique_idx += 1

        return unique_idx
