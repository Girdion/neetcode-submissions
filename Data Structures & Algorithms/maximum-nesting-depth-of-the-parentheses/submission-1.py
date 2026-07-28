class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        maxStack = 0
        lenStack = 0
        
        for char in s:

            if char == ')':
                stack.pop()
            elif char == '(':
                stack.append(char)
            
            lenStack = len(stack)

            maxStack = max(maxStack, lenStack)
        
        return maxStack

            

