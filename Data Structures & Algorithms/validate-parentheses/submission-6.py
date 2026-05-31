class Solution:
    def isValid(self, s: str) -> bool:
        prtsMap = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in prtsMap: 
                stack.append(ch)
            else: 
                if not stack or prtsMap[stack[-1]] != ch:
                    return False
             
                stack.pop()

        return not stack
