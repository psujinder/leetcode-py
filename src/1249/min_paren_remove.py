from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        s_list = list(s)

        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[idx] = ""

        while stack:
            s_list[stack.pop()] = ""

        return "".join(s_list)
