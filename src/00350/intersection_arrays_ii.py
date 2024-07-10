from typing import List


class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

    Time complexity:
        O(n + m) where n is the length of nums1 and m is the length of nums2

    Space complexity:
        O(min(n, m)) to store the frequency of elements from the smaller array
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        num_freq = {}
        result = []

        for num in nums1:
            num_freq[num] = num_freq.setdefault(num, 0) + 1

        for num in nums2:
            if num in num_freq and num_freq[num] > 0:
                result.append(num)
                num_freq[num] -= 1

        return result
