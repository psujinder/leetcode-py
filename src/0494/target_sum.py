from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        result = 0

        def backtrack(index: int, curr_path_sum: int):

            nonlocal result

            if index == len(nums):
                if curr_path_sum == target:
                    result += 1
                return

            backtrack(index + 1, curr_path_sum + nums[index])
            backtrack(index + 1, curr_path_sum - nums[index])

        backtrack(0, 0)
        return result
