class MinStack:

    def __init__(self):
        self.items = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        if val > self.minstack[-1]:
            self.minstack.append(self.minstack[-1])
    
    def pop(self) -> None:
        self.items.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
