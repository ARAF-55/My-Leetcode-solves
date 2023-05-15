class Solution:
    def myAtoi(self, s: str) -> int:
        state, sign, value = 0, 1, 0
        for i in range(len(s)):
            if state == 0:
                if s[i] == ' ':
                    state = 0
                elif s[i] == '+' or s[i] == '-':
                    if s[i] == '+':
                        sign = 1
                        state = 1
                    else:
                        sign = -1
                        state = 1
                elif s[i].isdigit():
                    state = 2
                    value = value * 10 + int(s[i])
                else:
                    return 0
            elif state == 1:
                if s[i].isdigit():
                    state = 2
                    value = value * 10 + int(s[i])
                else:
                    return 0
            elif state == 2:
                if s[i].isdigit():
                    state = 2
                    value = value * 10 + int(s[i])
                else:
                    break
        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)
        return value


solve = Solution()
val = solve.myAtoi("")
print(val)




