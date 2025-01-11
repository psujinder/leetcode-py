from typing import List


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/move-zeroes/description/

    This function moves all zeroes in the input list `nums` to the end of the list,
    while maintaining the relative order of the non-zero elements.

    Time Complexity: O(n)
        - The list is traversed twice. The first traversal processes each element to
          move non-zero elements forward, and the second traversal fills the remaining
          positions with zeroes. Both traversals are linear, making the overall time complexity O(n),
          where n is the number of elements in the list.

    Space Complexity: O(1)
        - The function operates in-place, modifying the input list directly without using additional
          space proportional to the size of the input. Thus, the space complexity is constant.
    """

    def moveZeroes(self, nums: List[int]) -> None:

        j = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0

        return nums
