class Solution:
    def __init__(self):
        self.symVal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s):
        val = 0
        if len(s) == 1:
            return self.symVal[s[0]]
        else:
            for i in range(len(s) - 1):
                if self.symVal[s[i]] >= self.symVal.get(s[i + 1]):
                    val += self.symVal[s[i]]
                else:
                    val -= self.symVal[s[i]]
            val += self.symVal.get(s[i + 1])
            return val


roman = Solution()
value = roman.romanToInt('XXIII')
print(value)
