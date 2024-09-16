import pytest
from check_n_double_exist import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("arr, result", [([10, 2, 5, 3], True), ([3, 1, 7, 11], False)])
def test_check_n_double(solution, arr, result):
    assert solution.checkIfExist(arr) == result
