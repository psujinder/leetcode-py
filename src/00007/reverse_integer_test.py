import pytest
from reverse_integer import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "x,expected_result",
    [
        (123, 321),
        (-123, -321),
        (120, 21),
    ],
)
def test_reverse_integer(solution, x, expected_result):

    result = solution.reverse(x)
    assert result == expected_result


if __name__ == "__main__":
    pytest.main()
