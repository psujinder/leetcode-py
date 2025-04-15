from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        result = []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, combination):
            if index == len(digits):
                result.append(combination)
                return

            letters = phone_map[digits[index]]
            for letter in letters:
                backtrack(index + 1, combination + letter)

        backtrack(0, "")
        return result
