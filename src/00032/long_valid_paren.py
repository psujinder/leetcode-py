class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/longest-valid-parentheses/

    This function calculates the length of the longest valid parentheses substring
    in the given string `s`.

    Approach:
    - Use a stack to track unmatched parentheses indices.
    - Initialize the stack with `-1` to serve as a base index for valid substrings.
    - For each character in the string:
        - If it's an opening bracket `(`, push its index onto the stack.
        - If it's a closing bracket `)`:
            - Pop the stack to check for a matching opening bracket.
            - If the stack becomes empty, push the current index as the new base.
            - Otherwise, calculate the length of the valid substring as the difference
              between the current index and the top of the stack.
    - Keep track of the maximum length of valid substrings during the iteration.

    Time Complexity: O(n)
        - Each character in the string is processed once, and stack operations (push/pop)
          are O(1), making the overall time complexity linear.

    Space Complexity: O(n)
        - The stack stores the indices of unmatched parentheses, requiring space
          proportional to the input string in the worst case.
    """

    def longestValidParentheses(self, s: str) -> int:

        max_len = 0
        stack = []
        stack.append(-1)

        for idx in range(len(s)):
            if s[idx] == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    max_len = max(max_len, idx - stack[-1])

        return max_len
