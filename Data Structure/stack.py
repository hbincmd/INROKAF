class ListStack:
    def __init__(self):
        self.data = list()

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()
    
stack = ListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.data)
print(stack.pop())
print(stack.pop())
