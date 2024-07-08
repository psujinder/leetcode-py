import pytest
from rotate_array import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, k, expected_nums",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_rotate_array(solution, nums, k, expected_nums):
    solution.rotate(nums, k)
    assert nums == expected_nums


if __name__ == "__main__":
    pytest.main()
