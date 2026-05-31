class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] == '+':
                stack.append(int(stack[-2]) + int(stack[-1]))
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                stack.append(int(stack[-1]) * 2)
            else:
                stack.append(operations[i])
        
        res = 0
        
        for num in stack:
            res += int(num)
        
        return res
        