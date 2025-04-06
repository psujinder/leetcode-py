import pytest
from max_consecutive_ones import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, count", [([1, 1, 0, 1, 1, 1], 3), ([1, 0, 1, 1, 0, 1], 2)]
)
def test_max_consecutive_ones(solution, nums, count):
    assert solution.findMaxConsecutiveOnes(nums) == count


if __name__ == "__main__":
    pytest.main()
