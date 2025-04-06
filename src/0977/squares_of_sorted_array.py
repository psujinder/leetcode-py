from typing import List


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/squares-of-a-sorted-array/

    Time Complexity: O(n)
        - we traverse the input list once linearly

    Space Complexity: O(n)
        - we use an array for the same lenght as the input list to store the result
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        position = right

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[position] = abs(nums[left]) ** 2
                left += 1
            else:
                result[position] = abs(nums[right]) ** 2
                right -= 1
            position -= 1

        return result
