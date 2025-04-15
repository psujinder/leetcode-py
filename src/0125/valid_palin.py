class Solution:
    def isPalindrome(self, s: str) -> bool:

        left_idx = 0
        right_idx = len(s) - 1
        s = s.lower()

        while left_idx < right_idx:

            while not s[left_idx].isalnum() and left_idx < right_idx:
                left_idx += 1

            while not s[right_idx].isalnum() and right_idx > left_idx:
                right_idx -= 1

            if s[left_idx] != s[right_idx]:
                return False

            left_idx += 1
            right_idx -= 1

        return True
