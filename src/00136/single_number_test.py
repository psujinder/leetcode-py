import pytest
from single_number import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected_num",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ],
)
def test_single_number(solution, nums, expected_num):
    assert solution.singleNumber(nums) == expected_num


if __name__ == "__main__":
    pytest.main()
