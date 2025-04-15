from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        result = []

        def backtrack(index: int, path: str, curr_path_sum: int, last_operand: int):

            if index == len(num):
                if curr_path_sum == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                if i > index and num[index] == "0":
                    break

                curr_str = num[index : i + 1]
                curr_int = int(curr_str)

                if index == 0:
                    backtrack(i + 1, curr_str, curr_int, curr_int)
                else:
                    backtrack(
                        i + 1, path + "+" + curr_str, curr_path_sum + curr_int, curr_int
                    )

                    backtrack(
                        i + 1, path + "-" + curr_str, curr_path_sum - curr_int, -curr_int
                    )

                    backtrack(
                        i + 1,
                        path + "*" + curr_str,
                        curr_path_sum - last_operand + last_operand * curr_int,
                        last_operand * curr_int,
                    )

        backtrack(0, "", 0, 0)
        return result
