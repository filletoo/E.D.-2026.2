class Queue:
    def __init__(self):
        self.itens = ['']*100
        self.pos = 0

    def push(self, item):
        self.itens[self.pos] = item
        self.pos += 1

    def pop(self):
        temp = self.itens[self.pos - 1]
        self.itens[self.pos - 1] = ''
        self.pos -= 1
        return temp
    
stack1 = Queue()
stack2 = Queue()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.push(7)

for i in range(stack1.pos):
    stack2.push(stack1.pop())

for i in range(stack2.pos):
    print(stack2.pop())
