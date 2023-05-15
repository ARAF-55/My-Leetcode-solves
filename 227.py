class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = '+'
        operations = '+-/*'
        currentVal = 0
        for i in range(len(s)):
            if s[i].isdigit():
                currentVal = currentVal * 10 + ord(s[i]) - ord('0')
            if s[i] in operations or i == len(s) - 1:
                if operator == '+':
                    stack.append(currentVal)
                elif operator == '-':
                    stack.append(-currentVal)
                elif operator == '*':
                    last_val = stack.pop()
                    stack.append(last_val * currentVal)
                else:
                    last_val = stack.pop()
                    stack.append(int(last_val / currentVal))
                operator = s[i]
                currentVal = 0
            i += 1
        return sum(stack)


solve = Solution()
print(solve.calculate("3+2*2"))
