from typing import List


class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/reverse-string/description/

    Time Complexity:
        O(n) as the input string is processed linearly only once

    Space complexity:
        O(1) as the string is reversed in place and no additional space is used
    """

    def reverseString(self, s: List[str]) -> None:

        left_idx = 0
        right_idx = len(s) - 1

        while left_idx < right_idx:
            s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
            left_idx += 1
            right_idx -= 1
