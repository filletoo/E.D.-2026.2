import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prox = None

class HashTable:
    def __init__(self, M):
        self.M = M
        self.n = 0
        self.table = [None]*M

    def _hash(self, key):
        return hash(key) % self.M

    def get(self, key):
        if key == None: return None

        valor_hash = self._hash(key)
        aux = self.table[valor_hash]

        while aux:
            if aux.key == key:
                return aux.value
            aux = aux.prox

        return None

    def put(self, key, value):
        if key == None or value == None:
            return
        
        novo_no = Node(key, value)
        valor_hash = self._hash(key)
        aux = self.table[valor_hash]
        
        while aux:
            if aux.key == key:
                aux.value = value
                return
            aux = aux.prox

        novo_no.prox = self.table[valor_hash]
        self.table[valor_hash] = novo_no

        self.n += 1

    def remove(self, key):
        if key == None: return

        valor_hash = self._hash(key)
        aux = self.table[valor_hash]

        if aux and aux.key == key:
            self.table[valor_hash] = None
            self.n -= 1
            return
        
        while aux:
            if aux.prox and aux.prox.key == key:
                aux.prox = aux.prox.prox
                self.n -= 1
                return
            aux = aux.prox

    def getMin(self):
        min = None
        for i in range(self.M):
            aux = self.table[i]

            while aux:
                if min == None:
                    min = aux.key

                elif aux.key < min:
                    min = aux.key

                aux = aux.prox

        return min

    def getMax(self):
        max = None
        for i in range(self.M):
            aux = self.table[i]

            while aux:
                if max == None:
                    max = aux.key

                elif aux.key > max:
                    max = aux.key

                aux = aux.prox

        return max

    def floor(self, key):
        if key == None: return
        alvo = None
        for i in range(self.M):
            aux = self.table[i]

            while aux:
                if alvo == None:
                    if aux.key <= key:
                        alvo = aux.key

                elif alvo < aux.key <= key:
                    alvo = aux.key

                aux = aux.prox

        return alvo
                    
    def ceil(self, value):
        if value == None: return

        alvo = None
        for i in range(self.M):
            aux = self.table[i]

            while aux:
                if alvo == None:
                    if aux.value >= value:
                        alvo = aux.valuekey

                elif alvo > aux.value >= value:
                    alvo = aux.value

                aux = aux.prox

        return alvo

    def busca_sequencial(self, key):
        for i in range(self.M):
            aux = self.table[i]

            while aux:
                if aux.key == key:
                    return aux.value
                aux = aux.prox

        return aux

    def quantidades(self):
        quant = 0
        vazio = 0
        for i in range(self.M):
            aux = self.table[i]
            if aux == None:
                vazio += 1

            while aux:
                quant += 1
                aux = aux.prox

        return quant, vazio

class ST:
    def __init__(self):
        self.tam = 10
        self.keys = [None]*self.tam
        self.values = [None]*self.tam
        self.quant = 0

    
    

ht = HashTable(16)

for i in range(50):
    key = random.randint(0, 50)
    value = random.randint(0, 10000)
    
    escolha = random.choice([0,1])

    print("Key:",key, ", Value:", value)
    
    ht.put(key, value)

print("n:", ht.n)
print("Min:", ht.getMin())
print("Max:", ht.getMax())
print("Key 17:", ht.get(17))
print("Floor 34.5:", ht.floor(34.5))
print("Ceil 37.9:", ht.ceil(37.9))
print("Busca 17:", ht.busca_sequencial(17))