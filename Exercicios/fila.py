class Map:
    def __init__(self):
        self.size = 100
        self.chaves = ['']*self.size
        self.itens = ['']*self.size

    def adicionar(self, chave, item):
        for i in range(self.size):
            if self.chaves[i] == '':
                self.chaves[i] = chave
                self.itens[i] = item

    def procurar(self, chave):
        for i in range(self.size):
            if self.chaves[i] == chave:
                return self.itens[i]

        return False

    def remover(self, chave):
        for i in range(self.size):
            if self.chaves[i] == chave:
                self.chaves[i] = ''
                self.itens[i] = ''
                return True
        return False


class Set:
    def __init__(self):
        self.itens = ['']*100

    def contem(self, item):
        for i in range(100):
            if self.itens[i] == item:
                return True
        return False

    def adicionar(self, item):
        if not self.contem(item):
            for i in range(100):
                if self.itens[i] == '':
                    self.itens[i] = item


mapa = Map()

mapa.adicionar("buceta", 5)
mapa.adicionar("pinto", 10)

print(mapa.procurar("buceta"))
print(mapa.procurar("carlos"))

mapa.remover("buceta")
print(mapa.procurar("buceta"))
