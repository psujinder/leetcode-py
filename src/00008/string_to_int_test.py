import pytest
from string_to_int import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, expected_result",
    [("42", 42), (" -042", -42), ("1337c0d3", 1337), ("0-1", 0), ("words and 987", 0)],
)
def test_string_to_int(solution, s, expected_result):
    result = solution.myAtoi(s)
    assert expected_result == result
