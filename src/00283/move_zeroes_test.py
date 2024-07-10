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
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1], [1, 0, 0]),
        ([4, 0, 5], [4, 5, 0]),
    ],
)
def test_contains_duplicate(solution, nums, expected_ans):
    solution.moveZeroes(nums)
    assert expected_ans == nums


if __name__ == "__main__":
    pytest.main()
