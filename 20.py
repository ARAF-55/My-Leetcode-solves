class Solution:
    def isValid(self, s: str) -> bool:
        h_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in h_map:
                stack.append(i)
            if i not in h_map:
                if not stack or h_map[stack[len(stack)-1]] != i:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False


solve = Solution()
print(solve.isValid("{([])}"))
