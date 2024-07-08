from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_idx = 1

        for curr_idx in range(1, len(nums)):
            if nums[curr_idx] != nums[curr_idx - 1]:
                nums[unique_idx] = nums[curr_idx]
                unique_idx += 1

        return unique_idx
