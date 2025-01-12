from typing import List


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/rotate-array/

    This function rotates the elements of the input list `nums` to the right by `k` steps.
    The rotation is performed in place without using extra space for another array.

    Parameters:
    -----------
    nums (List[int]): A list of integers to be rotated.
    k (int): The number of steps to rotate the array to the right.

    Returns:
    --------
    None: The input list `nums` is modified in place.

    Time Complexity:
    ----------------
    O(n): The list is traversed three times for reversing different parts.

    Space Complexity:
    -----------------
    O(1): The function uses a constant amount of additional space.

    Algorithm:
    ----------
    The function uses a three-step reversal approach:
    1. Reverse the entire array.
    2. Reverse the first `k` elements.
    3. Reverse the remaining `n - k` elements.
    This approach ensures that the array is rotated correctly to the right.

    Steps:
    ------
    - First, calculate `k % n` to handle cases where `k` is greater than the length of the array.
    - Reverse the entire array.
    - Reverse the first `k` elements.
    - Reverse the rest of the array starting from index `k`.

    Example:
    --------
    Input:
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
    Output:
        nums = [5, 6, 7, 1, 2, 3, 4]

    Edge Cases:
    -----------
    - If the array is empty, do nothing.
    - If `k` is 0 or a multiple of the array length, the array remains unchanged.
    - Handles scenarios where `k > len(nums)` by reducing `k` to `k % len(nums)`.

    """

    def rotate(self, nums: List[int], k: int) -> None:

        def swap_numbers(nums, left, right):

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k = k % n

        swap_numbers(nums, 0, n - 1)
        swap_numbers(nums, 0, k - 1)
        swap_numbers(nums, k, n - 1)
