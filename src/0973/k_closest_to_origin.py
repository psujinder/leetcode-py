from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            distance = point[0]**2 = point[1]**2
            distances.append((distance, point))

        distances.sort(key=lambda x:x[0])

        return [ val for _,val in distances[:k]]
