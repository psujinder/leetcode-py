from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_index = 1

        for curr_index in range(1, len(nums)):
            if nums[curr_index] != nums[curr_index - 1]:
                nums[unique_index] = nums[curr_index]
                unique_index += 1

        return unique_index
