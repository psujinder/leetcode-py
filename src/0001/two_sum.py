from typing import List


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/two-sum/description/

    This function returns the indices of the two numbers in the input list `nums`
    that add up to the given `target`.

    Time Complexity: O(n)
        - We traverse the entire list once, and each lookup or insetion into the hashtable takes
          O(1) on average, making the time complexity linear, where n is the number
          of elements in the list

    Space Complexity: O(n)
        - We use a hash table to store the indices of the elements we have seen so far.
          In the worst case, we store all n elements, so the space complexity is linear
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for idx, num in enumerate(nums):

            remaining = target - num

            if remaining in seen:
                return [seen[remaining], idx]

            seen[num] = idx

        return []
