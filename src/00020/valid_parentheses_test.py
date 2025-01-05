import pytest
from valid_parentheses import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, ans",
    [
        # Basic cases
        ("()", True),  # Simple valid case
        ("()[]{}", True),  # Mixed valid parentheses
        ("(]", False),  # Mismatched parentheses
        ("([)]", False),  # Nested mismatched parentheses
        ("{[]}", True),  # Valid nested parentheses
        # Edge cases
        ("", True),  # Empty string, considered valid
        ("[", False),  # Single unmatched opening bracket
        ("]", False),  # Single unmatched closing bracket
        ("(((", False),  # Only opening brackets
        ("}}}", False),  # Only closing brackets
        ("({})", True),  # Valid nested parentheses with multiple types
    ],
)
def test_valid_parentheses(solution, s, ans):
    assert solution.isValid(s) == ans


if __name__ == "__main__":
    pytest.main()
