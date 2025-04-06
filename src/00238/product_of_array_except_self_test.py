import pytest
from product_of_array_except_self import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),  # Standard case
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),  # Includes negative numbers
    ],
)
def test_product(nums, output):
    solution = Solution()
    ans = solution.productExceptSelf(nums)
    assert ans == output
