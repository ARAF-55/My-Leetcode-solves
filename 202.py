class Solution:
    def isHappy(self, n: int) -> bool:
        the_map = set()
        the_val = 0
        while n != 1:
            if n in the_map:
                return False
            the_map.add(n)
            while n // 10 != 0:
                the_val += (n % 10) ** 2
                n = n // 10
            the_val += (n % 10) ** 2
            n = the_val
            the_val = 0
        return True
