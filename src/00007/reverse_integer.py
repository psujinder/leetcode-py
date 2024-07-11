class Solution:
    """
    Leetcode problem link:
        https://leetcode.com/problems/reverse-integer/description/

    Time Complexity:
        O(log(n)) because the number of digits in the input number x determines the number of iterations

    Space Complexity:
        O(1) as constant additional space is being used
    """

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse_num = 0

        while x > 0:
            reverse_num = reverse_num * 10 + x % 10
            x = x // 10

        reverse_num *= sign

        if reverse_num > pow(2, 31) - 1 or reverse_num < -1 * pow(2, 31):
            return 0

        return reverse_num
