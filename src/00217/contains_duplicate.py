from typing import List

"""
Leetcode problem link
    https://leetcode.com/problems/contains-duplicate/description/

Time complexity
    O(n) as the array is traversed once linearly 
    
Space complexity
    O(n) as additional space is used to store elements in the set.
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
