from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        result = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1":
                    result += 1
                    grid[row][col] = "0"
                    queue = deque([(row, col)])

                    while queue:
                        r, c = queue.popleft()

                        for dr, dc in ([-1, 0], [1, 0], [0, -1], [0, 1]):

                            nr, nc = r + dr, c + dc
                            if (
                                0 <= nr < rows
                                and 0 <= nc < cols
                                and grid[nr][nc] == "1"
                            ):
                                grid[nr][nc] = 0
                                queue.append((nr, nc))

        return result
