class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        the_map = {}
        for i in s:
            if i not in the_map:
                the_map[i] = 1
            else:
                the_map[i] += 1

        for i in t:
            if i not in the_map:
                return False
            else:
                the_map[i] -= 1
                if the_map[i] == 0:
                    the_map.pop(i)
        return True


solve = Solution()
print(solve.isAnagram(s = "rat", t = "car"))
