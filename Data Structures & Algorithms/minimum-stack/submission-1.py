class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = math.inf
        self.min_count = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.minimum:
            self.minimum = val
            self.min_count = 1
        elif val==self.minimum:
            self.min_count+=1

    def pop(self) -> None:
        if len(self.stack)==0: return
        if self.stack[-1] == self.minimum:
            self.min_count-=1
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_count<=0:
            self.minimum = self.stack[0]
            for i in range(len(self.stack)):
                if self.stack[i]<self.minimum:
                    self.minimum = self.stack[i]
        return self.minimum