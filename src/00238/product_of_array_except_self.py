from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans_left = [None] * len(nums)
        ans_right = [None] * len(nums)
        ans = [None] * len(nums)

        ans_left[0] = 1
        ans_right[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            ans_left[i] = ans_left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            ans_right[i] = ans_right[i + 1] * nums[i + 1]

        for i in range(0, len(nums)):
            ans[i] = ans_left[i] * ans_right[i]

        return ans
