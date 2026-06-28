class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        stackMap = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for char in s:
            if stack and char in stackMap and stack[-1] == stackMap[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if not stack: return True
        else: return False
        
        