class PessoaNaFila:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome

class FilaArray:
    def __init__(self):
        #tamanhos
        self.tam = 2
        #filas com e sem prioridade
        self.fila = ['']*self.tam
        #indicadores Al 
        self.inicio = 0
        self.fim = -1
        self.quant = 0
        

    #redimensionar o array
    def redimensionar_fila(self):
        nova_fila = ['']*self.tam
        j = 0
        for i in range(self.inicio, self.fim + 1):
            if self.fila[i] != '':
                nova_fila[j] = self.fila[i]
                j += 1
        self.fila = nova_fila
        self.inicio = 0
        self.fim = j - 1
    
    def enqueue(self, pessoa):
        #ver se precisa redimensionar
        if self.quant == self.tam:
            self.tam *= 2
            self.redimensionar_fila()
        self.fila[self.fim + 1] = pessoa
        self.fim += 1
        self.quant += 1
        return pessoa
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("A fila está vazia")
        retorno = self.fila[self.inicio]
        self.fila[self.inicio] = ''
        self.inicio += 1
        self.quant -= 1
        # Redimensionar depois da remoção
        if self.quant <= self.tam // 4 and self.tam > 2:
            self.tam //= 2
            self.redimensionar_fila()
        return retorno
    
    def isEmpty(self):
        return self.quant == 0
    
    def PrintLista(self): 
        for i in range(self.inicio, self.fim + 1):
            if self.fila[i] != '':
                print(self.fila[i])