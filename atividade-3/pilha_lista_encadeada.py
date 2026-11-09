class Node:
    def __init__(self, val):
        self.item = val
        self.prox = None

class PilhaLista:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        aux = Node(item)
        aux.prox = self.top
        self.top = aux

    def pop(self):
        if self.isEmpty(): return None
        aux = self.top.item
        self.top = self.top.prox
        return aux

    def isEmpty(self):
        return self.top == None

    