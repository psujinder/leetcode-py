import pytest
from climbing_stairs import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("n, ans", [(2, 2), (3, 3)])
def test_climbing_stairs(solution, n, ans):
    assert solution.climbStairs(n) == ans


@pytest.mark.parametrize("n, ans", [(2, 2), (3, 3)])
def test_climbing_stairs2(solution, n, ans):
    assert solution.climbStairs2(n) == ans


if __name__ == "__main__":
    pytest.main()
