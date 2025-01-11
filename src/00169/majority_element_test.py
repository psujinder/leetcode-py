import pytest
from typing import List
from majority_element import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([6, 6, 6, 7, 7], 6),
        ([5, 5, 5, 5, 5], 5),
    ],
)
def test_majority_element(solution, nums, expected):
    assert solution.majorityElement(nums) == expected


if __name__ == "__main__":
    pytest.main()
