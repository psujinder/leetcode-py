from typing import List

"""
Time complexity : o(n) as all the elements of the array are processed one linearly
Space complexuty: o(1) as there is not additional space being consumed

"""


class Solution:
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
