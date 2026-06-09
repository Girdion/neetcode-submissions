class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[-1])
        res = []
        val = 0
        for token in tokens:
            if token == '+':
                val = int(res[-2]) + int(res[-1])
                res.pop()
                res.pop()
                res.append(val)
            elif token == '-':
                val = int(res[-2]) - int(res[-1])
                res.pop()
                res.pop()
                res.append(val)
            elif token == '*':
                val = int(res[-2]) * int(res[-1])
                res.pop()
                res.pop()
                res.append(val)
            elif token == '/':
                val = int(res[-2]) / int(res[-1])
                val = int(val)
                res.pop()
                res.pop()
                res.append(val)
            else:
                res.append(token)
        
        return res[-1]

        