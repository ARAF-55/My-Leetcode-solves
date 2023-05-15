class Solution:
    def climbStairs(self, n: int) -> int:
        global result
        result = 0

        def backtracking(value, the_dict):

            global result
            if value in the_dict:
                return the_dict[value]
            else:
                if value == n:
                    print("yes")
                    # result += 1
                    return 1
                if value < n:
                    the_dict[value] = backtracking(value+1, the_dict)
                if value < n - 1:
                    the_dict[value] += backtracking(value+2, the_dict)
                return the_dict[value]
        return backtracking(0, {})
        # return result


solve = Solution()
print(solve.climbStairs(17))
