from typing import List, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = Counter(nums)
        result = []

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count_map.items():
            buckets[freq].append(num)

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
