from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        min_distance = math.inf
        max_distance = -math.inf

        distance_map = {}

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if distance in distance_map:
                distance_map[distance].append(point)
            else:
                distance_map[distance] = [point]

            min_distance = min(min_distance, distance)
            max_distance = max(max_distance, distance)

        for distance in sorted(distance_map):
            for point in distance_map[distance]:
                result.append(point)

                if len(result) == k:
                    return result

        return result


if __name__ == "__main__":
    sol = Solution()
    result = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    print(result)
