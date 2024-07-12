import pytest
from valid_palindrome import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s,expected_result",
    [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)],
)
def test_valid_palindrome(solution, s, expected_result):
    result = solution.isPalindrome(s)
    assert expected_result == result
