class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = x
        result = 0

        while x > 0:
            result = result * 10 + (x % 10)
            x = x // 10

        return result == y
