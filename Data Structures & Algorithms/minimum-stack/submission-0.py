class MinStack:

    def __init__(self):
        self._stack = []
        self._minValue = []


    def push(self, value: int) -> None:
        self._stack.append(value)
        if not self._minValue:
            self._minValue.append(value)
        else:
            if self._minValue[-1] > value:
                self._minValue.append(value)
            else:
                self._minValue.append(self._minValue[-1])

    def pop(self) -> None:
        self._stack.pop()
        self._minValue.pop()

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self._minValue[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()