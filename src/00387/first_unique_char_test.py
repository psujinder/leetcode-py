import pytest
from first_unique_char import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, expected_result",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
    ],
)
def test_first_unique_char_in_string(solution, s, expected_result):
    result = solution.firstUniqChar(s)
    assert result == expected_result
