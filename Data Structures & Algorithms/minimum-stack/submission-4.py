class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.minVal = []
        self.minValSize = 0

    def push(self, val: int) -> None:
        if self.size == 0:
            self.minVal.append(val)
            self.minValSize += 1
        else:
            if val <= self.minVal[self.minValSize - 1]:
                self.minVal.append(val)
                self.minValSize += 1
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        if self.stack.pop() == self.minVal[self.minValSize - 1]:
            self.minVal.pop()
            self.minValSize -= 1
        self.size -= 1
            

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.minVal[self.minValSize - 1]
        
