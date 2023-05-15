from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        the_set = {'+', '-', '*', '/'}
        for i in tokens:
            if i not in the_set:
                stack.append(i)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if i == '+':
                    stack.append(int(operand1) + int(operand2))
                if i == '-':
                    stack.append(int(operand2) - int(operand1))
                if i == '*':
                    stack.append(int(operand1) * int(operand2))
                if i == '/':
                    stack.append(int(operand2) / int(operand1))
        return stack[0] if stack else int(tokens[0])


solve = Solution()
print(solve.evalRPN(["18"]))
