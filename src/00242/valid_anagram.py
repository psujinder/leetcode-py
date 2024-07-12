class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/valid-anagram/description/

    Time complexity:
        O(n) as the inputs are processed once linearly

    Space complexity:
        O(n) for the usage of the dictionary to maintain character frequencies
    """

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_freq = {}

        for s_char in s:
            char_freq[s_char] = char_freq.get(s_char, 0) + 1

        for t_char in t:
            if t_char not in char_freq:
                return False

            char_freq[t_char] -= 1
            if char_freq.get(t_char) == 0:
                del char_freq[t_char]

        return len(char_freq) == 0
