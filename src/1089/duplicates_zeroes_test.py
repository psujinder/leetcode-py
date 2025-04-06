import pytest
from duplicates_zeroes import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "arr, result",
    [([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]), ([1, 2, 3], [1, 2, 3])],
)
def duplicates_zeroes_test(solution, arr, result):
    assert solution.duplicateZeros(arr) == result


if __name__ == "__main__":
    pytest.main()
