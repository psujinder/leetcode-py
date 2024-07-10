import pytest
from intersection_arrays_ii import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums1, nums2, expected_nums",
    [
        ([1, 2, 2, 1], [2, 2], ([2, 2])),
        ([4, 9, 5], [9, 4, 9, 8, 4], ([9, 4], [4, 9])),
    ],
)
def test_intersection_array_ii(solution, nums1, nums2, expected_nums):
    result = solution.intersect(nums1, nums2)
    assert result in expected_nums


if __name__ == "__main__":
    pytest.main()
