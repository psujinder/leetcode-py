from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [[]]

        for num in nums:
            new_set = []
            for curr in result:
                new_set.append(curr + [num])
            result.extend(new_set)

        return result
