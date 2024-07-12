class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/string-to-integer-atoi/description/

    Time complexity:
        O(n) as the input string is traversed once linearly

    Space complexity:
        O(1) as a constant space is used to store the result
    """

    def myAtoi(self, s: str) -> int:

        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        result = 0
        idx = 0
        sign = 1

        # skip leading white spaces
        while idx < len(s) and s[idx] == " ":
            idx += 1

        # check if string is empty after removing leading white spaces and determine sign
        if idx < len(s) and s[idx] in ("-", "+"):
            sign = -1 if s[idx] == "-" else 1
            idx += 1

        while idx < len(s) and s[idx].isdigit():
            result = result * 10 + int(s[idx])
            idx += 1

        result *= sign

        if result > MAX_INT:
            result = MAX_INT
        elif result < MIN_INT:
            result = MIN_INT

        return result
