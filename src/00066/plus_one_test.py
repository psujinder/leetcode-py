import pytest
from plus_one import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "digits, expected_digits",
    [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
    ],
)
def test_plus_one(solution, digits, expected_digits):
    result = solution.plusOne(digits)
    assert result == expected_digits


if __name__ == "__main__":
    pytest.main()
