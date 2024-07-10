from typing import List
from collections import defaultdict


class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/valid-sudoku/description/

    Time complexity:
        O(1) since the board size is fixed at 9x9 and all the elements are processed only once

    Space complexity:
        O(1) the size of the additional storage space beause od rows, cols and boxes are also fixed because the board size is fixed
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]

                if num == ".":
                    continue

                box = (row // 3, col // 3)

                if num in rows[row] or num in cols[col] or num in boxes[box]:
                    return False
                else:
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

        return True
