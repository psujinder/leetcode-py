from typing import List


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/max-consecutive-ones/

    This function finds the maximum number of consecutive 1s in a binary array.

    Time Complexity: O(n)
        - We traverse the entire list once, so the time complexity is linear,
          where n is the number of elements in the list.

    Space Complexity: O(1)
        - We are only using two additional variables (max_count and curr_count),
          regardless of the input size, so the space complexity is constant.
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_count = 0
        curr_count = 0

        for num in nums:
            if num == 1:
                curr_count += 1
                max_count = max(curr_count, max_count)
            else:
                curr_count = 0

        return max_count
