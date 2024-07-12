class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

    Time complexity:
        O(m*n) as the outer loop runs for m times over the haystack and the inner loop runs n times over the needle

    Space complexity:
        O(1) as a constant additional space is used

    """

    def strStr(self, haystack: str, needle: str) -> int:

        # Initialize the starting index for haystack and needle
        haystack_idx = 0
        needle_idx = 0

        # If the needle is an empty string, return 0 as per problem statement
        if len(needle) == 0:
            return 0

        # Get the lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)

        # Iterate over the haystack
        while haystack_idx < haystack_len:
            # If the current character in haystack matches the first character in needle
            if haystack[haystack_idx] == needle[needle_idx]:

                # Use a temporary index to check for the rest of the needle
                tmp_haystack_idx = haystack_idx

                # Continue checking the subsequent characters in haystack and needle
                while (
                    tmp_haystack_idx < haystack_len
                    and needle_idx < needle_len
                    and haystack[tmp_haystack_idx] == needle[needle_idx]
                ):
                    tmp_haystack_idx += 1
                    needle_idx += 1

                # If we have checked all characters in the needle and they match
                # Return the starting index of the match
                if needle_idx == needle_len:
                    return haystack_idx

                # Reset needle index to 0 if not all characters matched
                needle_idx = 0

            # Move to the next character in haystack
            haystack_idx += 1

        # If no match is found, return -1
        return -1
