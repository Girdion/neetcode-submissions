class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                temp = []

                while stack and stack[-1] != '[':
                    temp.append(stack.pop())

                stack.pop()  

                num = []

                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                repeat = int("".join(num[::-1]))

                decoded = "".join(temp[::-1]) * repeat

                stack.append(decoded)

        return "".join(stack)