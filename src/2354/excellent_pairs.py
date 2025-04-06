from typing import List
from bisect import bisect_left


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/number-of-excellent-pairs/

    This function computes the number of excellent pairs in the input list `nums`.
    An excellent pair is defined as a pair (a, b) such that:
    - a and b are unique elements of `nums`
    - The sum of their Hamming weights (number of 1s in the binary representation)
      satisfies the condition: popcount(a) + popcount(b) >= k

    Steps:
    - Remove duplicates from `nums`.
    - Compute the Hamming weights for each unique element.
    - Sort the Hamming weights to enable binary search.
    - Use binary search to efficiently count all valid pairs.

    Time Complexity: O(n log n)
        - Removing duplicates: O(n)
        - Computing Hamming weights: O(n log(max)), where max is the largest number in `nums`
        - Sorting the Hamming weights: O(n log n)
        - Binary search for each weight: O(n log n)
        Total complexity is dominated by the sorting and binary search steps.

    Space Complexity: O(n)
        - We store the unique numbers and their corresponding Hamming weights,
          both of which require linear space in the worst case.
    """

    def countExcellentPairs(self, nums: List[int], k: int) -> int:

        count = 0
        unique_elements = set(nums)
        hamming_weights = [bin(unique_num).count("1") for unique_num in unique_elements]

        hamming_weights.sort()

        len_hamming_weights = len(hamming_weights)

        for hw in hamming_weights:

            small_idx = bisect_left(hamming_weights, k - hw)
            count += len_hamming_weights - small_idx

        return count
