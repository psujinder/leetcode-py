from typing import List


class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes_count = 0
        non_zeroes_count = 0
        n = len(arr)

        for i in range(len(arr)):
            if arr[i] == 0:
                zeroes_count += 1
            else:
                non_zeroes_count += 1

            if non_zeroes_count + (zeroes_count * 2) >= n:
                break

        right = n - 1
        idx = i

        while idx >= 0:
            if arr[idx] != 0:
                arr[right] = arr[idx]
                right -= 1
            else:
                arr[right] = 0
                if right - 1 >= 0:
                    arr[right - 1] = 0
                right -= 2
            idx -= 1

        return 0

    def duplicateZeros_1(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        n = len(arr)
        result = [0] * n
        position = 0

        for i in range(n):
            if arr[i] == 0:
                result[position] = 0
                if position + 1 < n:
                    result[position + 1] = 0
                else:
                    break
                position += 2
            else:
                result[position] = arr[i]
                position += 1

            if position >= n:
                break

        for i in range(n):
            arr[i] = result[i]


if __name__ == "__main__":
    sol = Solution()
    sol.duplicateZeros([8, 4, 5, 0, 0, 0, 0, 7])
