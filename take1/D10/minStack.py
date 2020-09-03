class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lis = []
        

    def push(self, x: int) -> None:
        self.lis.append(x)

    def pop(self) -> None:
        return self.lis.pop(len(self.lis)-1)

    def top(self) -> int:
        return self.lis[len(self.lis)-1]
        
    def getMin(self) -> int:
        minval = self.lis[0]
        for i in self.lis:
            if i <= minval:
                minval = i
        return minval
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
