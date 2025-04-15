from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:

        if nums == []:
            return [[lower, upper]]

        result = []

        if nums[0] > lower:
            result.append([lower, nums[0] - 1])

        idx = 0

        while idx < len(nums) - 1:
            if nums[idx] + 1 != nums[idx + 1]:
                result.append([nums[idx] + 1, nums[idx + 1] - 1])

            idx += 1

        if nums[len(nums) - 1] < upper:
            result.append([nums[len(nums) - 1] + 1, upper])

        return result
