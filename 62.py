class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path_finder(index1, index2, the_dict):
            if (index1, index2) in the_dict:
                return the_dict[(index1, index2)]
            else:
                if index1 == m - 1 and index2 == n - 1:
                    return 1
                elif index1 >= m or index2 >= n:
                    return 0
                else:
                    op1 = path_finder(index1 + 1, index2, the_dict)
                    op2 = path_finder(index1, index2 + 1, the_dict)
                    the_dict[(index1, index2)] = op1 + op2
                    return op1 + op2
        return path_finder(0, 0, {})


solve = Solution()
print(solve.uniquePaths(1, 1))
