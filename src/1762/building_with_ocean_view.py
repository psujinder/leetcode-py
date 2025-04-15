from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        max_height = heights[-1]
        result = [len(heights) - 1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                result.append(i)

        return result[::-1]
