import pytest
from excellent_pairs import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, k, ans",
    [
        # Basic cases
        ([1, 2, 3, 1], 3, 5),  # Example from explanation
        ([5, 1, 1], 10, 0),  # Basic case with distinct weights
        ([1, 2, 3], 3, 5),
    ],
)
def test_count_excellent_pairs(solution, nums, k, ans):
    assert solution.countExcellentPairs(nums, k) == ans


if __name__ == "__main__":
    pytest.main()
