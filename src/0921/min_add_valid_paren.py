
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        result = 0

        for ch in s:
            if ch == '(':
                stack.append('(')

            if ch == ')':
                if stack:
                    stack.pop()
                else:
                    result += 1
        
            
        return result + len(stack)
