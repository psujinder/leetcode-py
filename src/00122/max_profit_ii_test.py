import pytest
from max_profit_ii import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "prices, expected_profit",
    [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_max_profit(solution, prices, expected_profit):
    solution = Solution()

    max_profit = solution.maxProfit(prices)
    assert max_profit == expected_profit


if __name__ == "__main__":
    pytest.main()
