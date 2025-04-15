from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_map = {0: 1}
        result = 0
        sum = 0

        for num in nums:
            sum += num
            complement = sum - k

            if complement in sum_map:
                result += sum_map[complement]

            sum_map[sum] = sum_map.get(sum, 0) + 1

        return result
