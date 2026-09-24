class Solution:
    def isValid(self, s: str) -> bool:

        parenthesesMap = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for char in s:

            if stack and char in parenthesesMap and stack[-1] == parenthesesMap[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if not stack: return True

        return False
        
