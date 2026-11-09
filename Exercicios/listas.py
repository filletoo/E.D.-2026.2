class Node:
    def __init__(self, val):
        self.elem = val
        self.prox = None

class Lista:
    def __init__(self):
        self.inicio = None

    def isEmpty(self):
        return (self.inicio==None)
    
    def insert(self, el):
        novo = Node(el)
        novo.prox = self.inicio
        self.inicio = novo

    def remove(self, el):
        aux = self.inicio
        ant = self.inicio
        while (aux != None):
            if (aux.elem == el):
                if (aux==ant):
                    self.inicio = aux.prox
                else:
                    ant.prox = aux.prox
                return True
            else:
                ant = aux
                aux = aux.prox
        return False

    def countTwo(self):
        if self.isEmpty(): return 0
        quant = 0
        atual = self.inicio
        while (atual.prox != None):
            if atual.elem % 2 == 0:
                quant += 1
            atual = atual.prox

        if atual.prox == None and atual.elem % 2 == 0:
                    quant += 1
        return quant

    def soma(self):
        if self.isEmpty(): return 0
        soma = 0
        atual = self.inicio
        while (atual.prox != None):
            soma += atual.elem
            atual = atual.prox

        if atual.prox == None and atual.elem != None:
            soma += atual.elem
        return soma

    def vocabulario(self):
        listaVocab = Lista()
        if self.isEmpty(): return 0
        atual = self.inicio
        while (atual.prox != None):
            soma += atual.elem
            atual = atual.prox

        if atual.prox == None and atual.elem != None:
            soma += atual.elem
        return soma

lista = Lista()

print(lista.countTwo())
print(lista.soma())