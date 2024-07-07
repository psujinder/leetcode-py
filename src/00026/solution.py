from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        unique_idx = 0

        for curr_idx in range(1, len(nums)):
            if nums[unique_idx] != nums[curr_idx]:
                unique_idx += 1
                nums[unique_idx] = nums[curr_idx]

        return unique_idx + 1
