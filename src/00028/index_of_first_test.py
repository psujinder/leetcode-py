import pytest
from index_of_first import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "haystack, needle, expected_result",
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("mississippi", "issip", 4),
    ],
)
def test_index_of_first(solution, haystack, needle, expected_result):
    result = solution.strStr(haystack, needle)
    assert expected_result == result
