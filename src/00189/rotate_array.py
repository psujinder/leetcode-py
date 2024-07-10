from typing import List


class Solution:
    """
    Leetcode problem link
        https://leetcode.com/problems/rotate-array/description/

    Time complexity
        O(n) for reversing the entire array
        O(k) for reversing the first k elements
        O(n-k) for reversing the rest of the elements
        O(n) = o(n) + o(k) + o(n-k)

    Space complexity
        O(1) as the input array is modified in place
    """

    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(nums: List[int], start_idx: int, end_idx: int) -> None:

            left_idx = start_idx
            right_idx = end_idx

            while left_idx < right_idx:
                nums[left_idx], nums[right_idx] = (nums[right_idx], nums[left_idx])
                left_idx += 1
                right_idx -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
