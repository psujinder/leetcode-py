from typing import List


class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/two-sum/description/

    Time Complexity:
        O(n) as the input list is traversed only once linearly

    Space Complexity:
        O(n) beacause a dictionary is used to store each element of the input list along with its index
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], idx]
            else:
                seen[num] = idx

        return []
