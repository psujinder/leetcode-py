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

    def majorityElement(self, nums: List[int]) -> int:

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
