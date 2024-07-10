import pytest
from move_zeroes import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected_ans",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
    ],
)
def test_contains_duplicate(solution, nums, expected_ans):
    assert expected_ans == solution.moveZeroes(nums)


if __name__ == "__main__":
    pytest.main()
