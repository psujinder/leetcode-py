from typing import List


class Solution:
    """
    Leetcode problem link :
        https://leetcode.com/problems/rotate-image/description/

    Time complexity:
        O(n2). During transpose the the outer loop runs n times and the inner loop runs n/2 times.
        During reverse the outer loop runs n times and the inner loop runs n/2 times

    Space complexity:
        O(1) as not additional space is used
    """

    def rotate(self, matrix: List[List[int]]) -> None:

        def transpose(matrix: List[List[int]]) -> None:
            for row in range(len(matrix)):
                for col in range(row, len(matrix[0])):
                    matrix[row][col], matrix[col][row] = (
                        matrix[col][row],
                        matrix[row][col],
                    )

        def reverse(matrix: List[List[int]]) -> None:
            for row in range(len(matrix)):
                left = 0
                right = len(matrix[row]) - 1
                while left < right:
                    matrix[row][left], matrix[row][right] = (
                        matrix[row][right],
                        matrix[row][left],
                    )
                    left += 1
                    right -= 1

        transpose(matrix)
        reverse(matrix)
