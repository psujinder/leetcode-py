from typing import List


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/majority-element/description/

    This function finds the majority element in the input list `nums`. The majority element
    is the element that appears more than ⌊n / 2⌋ times, where n is the size of the list.

    The implementation uses the Boyer-Moore Voting Algorithm, which identifies the majority
    element in linear time and constant space.

    Time Complexity: O(n)
        - The list is traversed once, making the time complexity linear, where n is the number
            of elements in the list.

    Space Complexity: O(1)
        - The function uses a constant amount of additional space.
    """

    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
