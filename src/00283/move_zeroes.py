from typing import List


class Solution:
    """
    Leetcode problem link
        https://leetcode.com/problems/move-zeroes/description/

    Time complexity
        O(n) as the array is traversed once linearly

    Space complexity
        O(1) as constact space is used
    """

    def moveZeroes(self, nums: List[int]) -> None:

        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        for i in range(i, len(nums)):
            nums[i] = 0

        return nums
