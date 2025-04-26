from typing import List, Counter


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count_map.items():
            bucket[freq].append(num)

        result = []

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


if __name__ == "__main__":
    sol = Solution()
    result = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(result)
