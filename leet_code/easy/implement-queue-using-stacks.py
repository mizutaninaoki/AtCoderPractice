class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        # 数字(int)をリストに追加するため、数字の後に「,」が必要！！
        self.queue += x,

    def pop(self) -> int:
        first = self.queue[0]
        self.queue = self.queue[1:]
        return first

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# void push(int x) 要素xをキューの後方に押し出す。
# int pop() 要素をキューの先頭から削除して返す。
# int peek() キューの先頭にある要素を返す。
# boolean empty() キューが空の場合にtrueを、それ以外の場合にfalseを返します。
