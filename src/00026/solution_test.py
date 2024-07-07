import pytest


@pytest.mark.parametrize(
    "solution, nums, expected_length, expected_nums",
    [
        ("00026", [1, 1, 2], 2, [1, 2]),
        ("00026", [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ("00026", [], 0, []),
        ("00026", [1, 1, 1, 1, 1], 1, [1]),
        ("00026", [1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ],
    indirect=["solution"],
)
def test_remove_duplicates(solution, nums, expected_length, expected_nums):
    length = solution.removeDuplicates(nums)
    assert length == expected_length
    assert nums[:length] == expected_nums


if __name__ == "__main__":
    pytest.main()
