from typing import List


class Solution:
    """
    Leetcode Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    This function calculates the maximum profit that can be achieved from a single buy
    and sell operation in the stock market, given the prices of a stock on different days.

    The goal is to find the pair of days (buy and sell) such that the profit is maximized,
    where the buying day occurs before the selling day.

    Parameters:
    -----------
    prices (List[int]): A list of integers representing the stock price on each day.

    Returns:
    --------
    int: The maximum profit that can be achieved. If no profit is possible, returns 0.

    Time Complexity:
    ----------------
    O(n): The list is traversed once to calculate the maximum profit.

    Space Complexity:
    -----------------
    O(1): The function uses a constant amount of additional space.

    Algorithm:
    ----------
    - Initialize the `buy` and `sell` prices to the first day's price.
    - Initialize `max_profit` to 0.
    - Iterate through the list of prices:
        - If the current price is lower than `buy`, update both `buy` and `sell` to the current price.
        - If the current price is higher than `sell`, update `sell` and calculate the profit.
        - Update `max_profit` if the new profit is higher than the previous `max_profit`.
    - Return `max_profit` at the end of the iteration.

    Example:
    --------
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6).

    Edge Cases:
    -----------
    - If the list is empty or contains a single price, the profit is 0.
    - If the prices only decrease, the profit is 0.
    - If all prices are the same, the profit is 0.
    """

    def maxProfit(self, prices: List[int]) -> int:

        sell, buy, max_profit = prices[0], prices[0], 0

        for price in prices:

            if price < buy:
                sell, buy = price, price
            elif price > sell:
                sell = price
                max_profit = max(max_profit, sell - buy)

        return max_profit
