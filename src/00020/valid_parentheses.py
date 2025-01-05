class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/valid-parentheses/

    This function checks whether a given string `s` of parentheses is valid.
    A string is considered valid if:
    - Every opening bracket has a corresponding closing bracket.
    - Brackets are closed in the correct order.

    Approach:
    - Use a stack to track unmatched opening brackets.
    - For each character in the string:
        - If it is a closing bracket, check if the top of the stack has the matching opening bracket.
        - If it is an opening bracket, push it onto the stack.
    - After processing, the stack should be empty for the string to be valid.

    Time Complexity: O(n)
        - Each character in the string is processed exactly once, and stack operations
          (push and pop) are O(1).

    Space Complexity: O(n)
        - In the worst case, the stack stores all opening brackets, leading to linear space usage.
    """

    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        paren_mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for paren in s:
            if paren in paren_mapping:
                if not stack or stack[-1] != paren_mapping[paren]:
                    return False
                stack.pop()
            else:
                stack.append(paren)

        return len(stack) == 0
