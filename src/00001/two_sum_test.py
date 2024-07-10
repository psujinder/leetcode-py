import pytest
from two_sum import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, target, expected_nums",
    [
        ([2, 7, 11, 15], 9, ([0, 1], [1, 0])),
        ([3, 2, 4], 6, ([1, 2], [2, 1])),
        ([3, 3], 6, ([0, 1], [1, 0])),
    ],
)
def test_remove_duplicates(solution, nums, target, expected_nums):

    assert solution.twoSum(nums, target) in expected_nums


if __name__ == "__main__":
    pytest.main()
