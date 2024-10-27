class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs2(self, n: int) -> int:

        if n <= 2:
            return n

        curr = 0
        curr_minus_1 = 1
        curr_minus_2 = 2

        for _ in range(3, n + 1):
            curr = curr_minus_1 + curr_minus_2
            curr_minus_2 = curr_minus_1
            curr_minus_1 = curr

        return curr
