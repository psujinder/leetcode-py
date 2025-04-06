import pytest
from buy_and_sell_stock import Solution


@pytest.mark.parametrize(
    "prices, expected_profit",
    [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),  # No profitable transactions
        ([1, 2, 3, 4, 5], 4),  # Buy at 1, sell at 5
        ([2, 4, 1], 2),  # Buy at 2, sell at 4
        ([3, 3, 3, 3], 0),  # All prices are the same
        ([6, 1, 3, 2, 4, 7], 6),  # Buy at 1, sell at 7
        ([5, 4, 3, 2, 1, 6], 5),  # Buy at 1, sell at 6
    ],
)
def test_maxProfit(prices, expected_profit):
    solution = Solution()
    assert solution.maxProfit(prices) == expected_profit
