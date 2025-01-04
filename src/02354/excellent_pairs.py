from typing import List
from bisect import bisect_left


class Solution:
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
