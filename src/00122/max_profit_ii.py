from typing import List


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
