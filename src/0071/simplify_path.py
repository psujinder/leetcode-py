class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or part == "":
                continue
            else:
                stack.append(part)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    result = sol.simplifyPath("/home/")
    print(result)
