import pytest
from remove_duplicates import Solution


@pytest.mark.parametrize(
    "nums, expected_nums, expected_length",
    [
        ([1, 1, 2], [1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
        ([1, 1, 1], [1], 1),
        ([1, 2, 3], [1, 2, 3], 3),
        ([1], [1], 1),
        ([], [], 0),
    ],
)
def test_removeDuplicates(nums, expected_nums, expected_length):
    solution = Solution()
    # Call the method
    length = solution.removeDuplicates(nums)

    # Validate the returned length
    assert length == expected_length

    # Validate the content of nums (up to the returned length)
    assert nums[:length] == expected_nums
