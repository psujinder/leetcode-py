from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            else:
                last_seen[num] = i

        return False

    def containsNearbyDuplicateSet(self, nums: List[int], k: int) -> bool:

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False
