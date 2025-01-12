import pytest
from rotate_array import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # Standard case
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),  # Includes negative numbers
        ([1], 0, [1]),  # Single element, no rotation
        ([1], 1, [1]),  # Single element, k=1
        ([1, 2], 3, [2, 1]),  # Small list, k > len(nums)
        ([1, 2, 3], 0, [1, 2, 3]),  # No rotation
        ([1, 2, 3], 6, [1, 2, 3]),  # k is a multiple of len(nums)
    ],
)
def test_rotate(nums, k, expected):
    solution = Solution()
    solution.rotate(nums, k)
    assert nums == expected
