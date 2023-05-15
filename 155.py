class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, value):
        if value < self.min_val:
            self.stack.append((value, value))
            self.min_val = value
        else:
            self.stack.append((value, self.min_val))

    def pop(self):
        self.stack.pop()
        self.min_val = self.stack[len(self.stack)-1][1]
        if not self.stack:
            self.min_val = float('inf')

    def top(self):
        return self.stack[len(self.stack)-1][0]

    def getMin(self):
        return self.stack[len(self.stack)-1][1]


