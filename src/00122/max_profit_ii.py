from typing import List


class Solution:
    """
    Leetcode problem link
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

    Time complexity
        O(n) as input array is traversed once linearly

    Space complexuty
        O(1) as there is no additional space being consumed
    """

    def maxProfit(self, prices: List[int]) -> int:

        total_profit = 0
        buy_price = prices[0]

        for idx in range(1, len(prices)):
            if prices[idx] > buy_price:
                total_profit += prices[idx] - buy_price
                buy_price = prices[idx]
            else:
                buy_price = prices[idx]

        return total_profit
