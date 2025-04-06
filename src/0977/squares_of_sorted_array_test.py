import pytest
from squares_of_sorted_array import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,target",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_squares_of_sorted_array(solution, nums, target):
    assert solution.sortedSquares(nums) == target


if __name__ == "__main__":
    pytest.main()
