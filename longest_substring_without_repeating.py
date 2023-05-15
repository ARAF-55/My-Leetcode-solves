class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        value = 0
        the_string = ''
        for i in s:
            if i not in the_string:
                the_string += i
                if value < len(the_string):
                    value = len(the_string)
            elif i in the_string:
                the_string = the_string[the_string.find(i)+1:]
                the_string += i
        return value


solve = Solution()
output = solve.lengthOfLongestSubstring("dvdf")
print(output)
