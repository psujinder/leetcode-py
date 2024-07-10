import pytest
from reverse_string import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s,expected_result",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ],
)
def test_reverse_string(solution, s, expected_result):
    solution.reverseString(s)
    assert s == expected_result
