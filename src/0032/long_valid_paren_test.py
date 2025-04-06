import pytest
from long_valid_paren import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, ans",
    [
        # Basic cases
        ("(()", 2),  # Longest valid substring: "()"
        (")()())", 4),  # Longest valid substring: "()()"
        ("", 0),  # Empty string, no valid parentheses
        # Edge cases
        ("(", 0),  # Single opening bracket
        (")", 0),  # Single closing bracket
        ("()(()", 2),  # Longest valid substring: "()"
        ("(()))", 4),  # Longest valid substring: "(())"
        # Complex cases
        ("(()())", 6),  # Entire string is valid
        ("))((()())", 6),  # Longest valid substring: "(()())"
        ("(()(()))", 8),  # Entire string is valid
        ("()(()))))", 6),  # Longest valid substring: "(()(()))"
    ],
)
def test_longest_valid_parentheses(solution, s, ans):
    assert solution.longestValidParentheses(s) == ans


if __name__ == "__main__":
    pytest.main()
