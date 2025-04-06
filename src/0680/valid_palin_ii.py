class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalin(s, left, right):

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        l_idx = 0
        r_idx = len(s) - 1

        while l_idx < r_idx:
            if s[l_idx] != s[r_idx]:
                return isPalin(l_idx + 1, r_idx) or isPalin(l_idx, r_idx - 1)

            l_idx += 1
            r_idx -= 1

        return True
