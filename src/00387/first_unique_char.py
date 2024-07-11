from collections import defaultdict


class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/first-unique-character-in-a-string/description/

    Time Complexity:
        O(n) as the input string is proessed once linearly

    Space Complexity:
        O(n) for the usage of the dictionary for maintaining the mapping between characters in the string and their index
    """

    def firstUniqChar(self, s: str) -> int:

        char_idxs = {}

        for idx, character in enumerate(s):
            if character in char_idxs:
                char_idxs[character].append(idx)
            else:
                char_idxs[character] = [idx]

        for key, value in char_idxs.items():
            if len(value) == 1:
                return value[0]

        return -1
