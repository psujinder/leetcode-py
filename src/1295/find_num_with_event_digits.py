from typing import List


class Solution:
    """

    Leetcode Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits

    This class provides a solution to the problem of finding how many numbers
    in a list contain an even number of digits.

    Time Complexity: O(n * d)
        - where 'n' is the number of elements in the list and 'd' is the number of digits in the largest number (since we convert each number to a string to check its length).

    Space Complexity: O(1)
        - we use constant additional space regardless of the size of the input list.
    """

    def findNumbers(self, nums: List[int]) -> int:

        return sum(1 for num in nums if self._containsEvenDigits(num))

    def _containsEvenDigits(self, num):

        return len(str(num)) % 2 == 0
