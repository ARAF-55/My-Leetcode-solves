class Solution:
    class Vector2D:
        def __init__(self, vector_2d):
            self.vector_2d = vector_2d
            self.rows = len(vector_2d)
            self.cols = len(vector_2d[0])
            self.r = 0
            self.c = 0
            self.yes_next = True

        def next(self):
            if self.yes_next:
                temp = self.vector_2d[self.r][self.c]
                self.c += 1
                if self.r == self.rows - 1 and self.c == self.cols:
                    self.yes_next = False
                    return temp
                elif self.c == self.cols:
                    self.c = 0
                    self.r += 1
                    return temp
                return temp
            return None

        def has_next(self):
            return self.yes_next

