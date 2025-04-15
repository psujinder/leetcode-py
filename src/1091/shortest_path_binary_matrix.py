from typing import List
from collections import dequeu


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        path_len = math.inf

        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1

        visited = set()
        queue = deque()
        queue.append((0, 0, 1))

        directions = (
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1],
        )

        while queue:
            row, col, curr_path_len = queue.popleft()

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == rows - 1 and col == cols - 1:
                path_len = min(path_len, curr_path_len)
                break

            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]

                if (
                    new_row < 0
                    or new_row > rows - 1
                    or new_col < 0
                    or new_col > cols - 1
                    or [new_row, new_col] in visited
                    or grid[new_row][new_col] == 1
                ):
                    continue

                queue.append((new_row, new_col, curr_path_len + 1))

        return path_len if path_len != math.inf else -1
