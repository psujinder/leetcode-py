from typing import List


class Solution:
    """
    Leetcode problem link
        https://leetcode.com/problems/single-number/description/

    Time complexity
        O(n) for reversing the entire array

    Space complexity
        O(1) as no additional space is used
    """

    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            result = result ^ num

        return result
