class Node:
    def __init__(self, item):
        self.item = item
        self.prox = None

class ListaSimples:
    def __init__(self):
        self.inicio = None
        self.tam = 0

    def isEmpty(self):
        if self.inicio == None:
            return True
        else:
            return False
        
    def push(self, item):
        Novo_no = Node(item)
        Novo_no.prox = self.inicio
        self.inicio = Novo_no
        self.tam += 1
        return True

    def pop(self):
        if self.isEmpty(): return False
        temp = self.inicio
        self.inicio = self.inicio.prox
        return temp.item

    
stack = ListaSimples()

stack.push(5)
stack.push(6)
print(stack.pop())
stack.push(7)
print(stack.pop())
print(stack.pop())
    