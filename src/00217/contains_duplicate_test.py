import pytest
from contains_duplicate import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected_ans",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(solution, nums, expected_ans):
    assert expected_ans == solution.containsDuplicate(nums)


if __name__ == "__main__":
    pytest.main()
