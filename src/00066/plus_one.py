from typing import List


class Solution:
    """
    Leetcode problem link
        https://leetcode.com/problems/plus-one/description/

    Time complexity:
        O(n) as the input array is traversed one linearly

    Space complexity:
        O(1) as constant additional space is being used
    """

    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            new_digit = digits[i] + carry
            digits[i] = new_digit % 10
            carry = new_digit // 10

        return [1] + digits if carry == 1 else digits
