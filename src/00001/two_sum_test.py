import pytest
from two_sum import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, target, ans",
    [
        # Basic cases
        ([2, 7, 11, 15], 9, [0, 1]),  # Two numbers add up to target
        ([3, 2, 4], 6, [1, 2]),  # Multiple numbers with one valid pair
        ([3, 3], 6, [0, 1]),  # Two identical numbers add up to target
        # Edge cases
        ([1], 2, []),  # Single element, no solution
        ([3, 3], 9, []),  # Two identical numbers, no valid pair
        ([], 5, []),  # Empty list, no solution
        ([0, 4, 3, 0], 0, [0, 3]),  # Target is 0 with two 0s in the list
        ([5, 75, 25], 100, [1, 2]),  # Non-contiguous elements form the target
    ],
)
def test_two_sum(solution, nums, target, ans):
    assert solution.twoSum(nums, target) == ans


if __name__ == "__main__":
    pytest.main()
