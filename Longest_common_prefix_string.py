from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = strs[0]
        for i in strs:
            if len(i) < len(minimum):
                minimum = i
        if minimum == "":
            return ""
        for i in range(len(minimum)):
            for j in strs:
                if minimum[i] != j[i]:
                    if i == 0:
                        return ""
                    else:
                        return minimum[0:i]
        return minimum


prefix = Solution()
value = prefix.longestCommonPrefix(["ab", "a"])
print(value)
