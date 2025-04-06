import pytest
from move_zeroes import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 2, 3, 0, 0], [1, 2, 3, 0, 0]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 0, 0, 2, 3], [1, 2, 3, 0, 0]),
    ],
)
def test_move_zeroes(solution, nums, expected):
    solution.moveZeroes(nums)
    assert nums == expected


if __name__ == "__main__":
    pytest.main()
