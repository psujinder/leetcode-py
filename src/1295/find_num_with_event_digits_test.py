import pytest
from find_num_with_event_digits import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,count", [([12, 345, 2, 6, 7896], 2), ([555, 901, 482, 1771], 1)]
)
def test_find_num_with_even_digits(solution, nums, count):
    assert solution.findNumbers(nums) == count


if __name__ == "__main__":
    pytest.main()
