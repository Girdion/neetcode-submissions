class Solution:
    def isValid(self, s: str) -> bool:

        bracketMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for char in s:
            if char in bracketMap and not stack:
                return False
            elif char in bracketMap and stack[-1] == bracketMap[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if not stack:
            return True
        
        return False
        