from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        seen = set()
        isFound = False

        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                isFound = True
                break

            seen.add(num)

        return isFound
