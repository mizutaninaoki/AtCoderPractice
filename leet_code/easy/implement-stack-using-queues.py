class MyStack:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue += x,
        

    def pop(self) -> int:
        tmp = self.queue[-1]
        self.queue = self.queue[:-1]
        return tmp
        

    def top(self) -> int:
        return self.queue[-1]

        

    def empty(self) -> bool:
        return False if len(self.queue) else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()