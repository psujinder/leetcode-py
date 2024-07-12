import pytest
from valid_anagram import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s,t,expected_result",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_valid_anagram(solution, s, t, expected_result):
    result = solution.isAnagram(s, t)
    assert result == expected_result
