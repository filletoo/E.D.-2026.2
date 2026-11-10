import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button, Slider

import re

LARGURA = 0.08
ALTURA = 0.06
GAP = LARGURA + 0.03
MAX_POR_LINHA = 7

INICIO_BOTOES1 = 0.285
INICIO_BOTOES2 = 0.12
INICIO_BOTOES3 = 0.24

AMARELO = 'yellow'
VERDE = 'green'
NORMAL = 'lightblue'
CONTORNO_NORMAL = 'black'
VERMELHO = 'red'
COR_VOLTAR = "#ff4f4f"

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.estilo = {'cor': NORMAL, 'contorno': CONTORNO_NORMAL}

class BST:
    def __init__(self):
        self.raiz = None

        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(bottom=0.38)

        #cid = self.fig.canvas.mpl_connect('button_press_event', onclick)

        #Caixa de texto
        ax_texto = self.fig.add_axes([0.32, 0.29, 0.35, 0.05])
        self.textbox = TextBox(ax_texto, "Entrada: ")

        self.mensagem = self.fig.text(0.32, 0.35, '', size=13)

        #botões
        self.principal = []
        self.menu1 = []
        self.menu2 = []
        self.menu3 = []

        #fazer ignorar o resize event
        self.fig.canvas.callbacks.callbacks['resize_event'].clear()

        self.criar_botao("Put e Get", self.principal, 0.15, self.menu1_input)

        self.criar_botao("Estatisticas", self.principal, 0.15, self.menu2_input)

        self.criar_botao("Travessias", self.principal, 0.15, self.menu3_input)

        self.criar_botao("Limpar", self.principal, 0.15, self.limpar)
        
        #----------------------
        self.criar_botao("Inserir", self.menu1, 0.15, self.put_input)

        self.criar_botao("Ler arquivo", self.menu1, 0.15, self.ler_arquivo)

        self.criar_botao("Buscar", self.menu1, 0.15, self.get_input)

        self.criar_botao("Voltar", self.menu1, 0.15, self.voltar, COR_VOLTAR)

        #--------------------
        self.criar_botao("Menor Valor", self.menu2, 0.15, self.menorValor_input)

        self.criar_botao("Maior Valor", self.menu2, 0.15, self.maiorValor_input)

        self.criar_botao("Profundidade", self.menu2, 0.15, self.profundidade_input)

        self.criar_botao("Altura", self.menu2, 0.15, self.height_input)

        self.criar_botao("Comprimento", self.menu2, 0.15, self.comprimento_interno_input)

        self.criar_botao("Tamanho", self.menu2, 0.15, self.tamanho_input)
        
        self.criar_botao("Balanceada", self.menu2, 0.15, self.balanceada_input)

        self.criar_botao("Voltar", self.menu2, 0.06, self.voltar, COR_VOLTAR)

        #-------------------
        
        self.criar_botao("Pré-Ordem", self.menu3, 0.15, self.pre_ordem_input)

        self.criar_botao("Em-Ordem", self.menu3, 0.15, self.em_ordem_input)

        self.criar_botao("Pós-Ordem", self.menu3, 0.15, self.pos_ordem_input)

        self.criar_botao("Por níveis", self.menu3, 0.15, self.por_niveis_input)

        self.criar_botao("Voltar", self.menu3, 0.15, self.voltar, COR_VOLTAR)

        self.visibilidade_principal(True)

        self.desenhar()

    def criar_botao(self, nome, menu, pos_y, funcao, cor = 'lightgray'):
        if menu is self.menu1: inicio = INICIO_BOTOES1
        elif menu is self.menu2: inicio = INICIO_BOTOES2
        elif menu is self.menu3: inicio = INICIO_BOTOES3
        elif menu is self.principal: inicio = INICIO_BOTOES1

        posicao = [inicio + (len(menu) % MAX_POR_LINHA)*GAP, pos_y, LARGURA, ALTURA]

        ax_botao: plt.Axes = self.fig.add_axes(posicao)

        botao = Button(ax_botao, nome, hovercolor="#707070", color=cor)
        botao.on_clicked(funcao)

        menu.append((ax_botao, botao))

    def visibilidade_principal(self, visivel=True):
        for a, b in self.principal:
            a.set_visible(visivel)
            b.set_active(visivel)

        for a, b in self.menu1:
            a.set_visible(False)
            b.set_active(False)

        for a, b in self.menu2:
            a.set_visible(False)
            b.set_active(False)

        for a, b in self.menu3:
            a.set_visible(False)
            b.set_active(False)

        #self.desenhar()

    def menu1_input(self, evento):
        self.visibilidade_principal(False)
        
        for a, b in self.menu1:
            a.set_visible(True)
            b.set_active(True)

        self.desenhar()

    def menu2_input(self, evento):
        self.visibilidade_principal(False)

        for a, b in self.menu2:
            a.set_visible(True)
            b.set_active(True)

        self.desenhar()

    def menu3_input(self, evento):
        self.visibilidade_principal(False)

        for a, b in self.menu3:
            a.set_visible(True)
            b.set_active(True)

        self.desenhar()

    def voltar(self, evento):
        self.visibilidade_principal(True)
        self.limpar_estilos()
        self.desenhar()

    def limpar(self, evento):
        self.raiz = None

        self.mensagem.set_text("Árvore limpa!")

        self.desenhar(pausas=False)

    def limpar_estilo(self, no: Node):
        no.estilo['cor'] = NORMAL
        no.estilo['contorno'] = 'black'

    def ler_arquivo(self, evento):
        self.limpar_estilos()
        try:
            arquivo = self.textbox.text.strip()
            numeros = []
            with open(arquivo, "r") as f:
                numeros = re.split(r"[ ,\n]+", f.read().strip())

            for i in range(len(numeros)):
                numeros[i] = int(numeros[i])

            self.put_array(numeros)

            self.textbox.set_val("")

            self.limpar_estilos()
            self.mensagem.set_text("Arquivo lido com sucesso")
            self.fig.canvas.draw_idle()
            self.desenhar()
            
        except ValueError:
            self.mensagem.set_text("Há entradas não válidas no seu arquivo")

        except FileNotFoundError:
            self.mensagem.set_text("O arquivo não foi encontrado")

        except:
            self.mensagem.set_text("Um erro inesperado ocorreu")

    def put(self, key, no: Node = None, pausas=True):
        if self.isEmpty():
            self.raiz = Node(key)
            return True

        if no == None:
            no = self.raiz

        if key == no.key:
            no.estilo['cor'] = VERMELHO
            self.desenhar(pausas)
            
            return False

        else:
            no.estilo['cor'] = AMARELO
            self.desenhar(pausas)
            
            if key < no.key:
                if no.left == None:
                    no.left = Node(key)
                    no.left.estilo['cor'] = VERDE
                    self.desenhar(pausas)
                    return True
                else:
                    return self.put(key, no.left, pausas)

            else:
                if no.right == None:
                    no.right = Node(key)
                    no.right.estilo['cor'] = VERDE
                    self.desenhar(pausas)
                    return True
                else:
                    return self.put(key, no.right, pausas)

    def put_array(self, array, pausas=False):
        for i in range(len(array)):
            self.limpar_estilos()
            self.put(array[i], pausas=pausas)

    def put_input(self, evento):
        self.limpar_estilos()
        try:
            numeros = re.split(r"[, ]+", self.textbox.text.strip())

            for i in range(len(numeros)):
                numeros[i] = int(numeros[i])

            if len(numeros) > 1:
                self.put_array(numeros, pausas=True)

            else:
                res = self.put(numeros[0])
                if res:
                    self.mensagem.set_text(f"{numeros[0]} foi inserido")
                else:
                    self.mensagem.set_text(f"{numeros[0]} já existe")

            self.textbox.set_val("")

        except ValueError:
            self.mensagem.set_text("Digite um número inteiro válido!")

        self.fig.canvas.draw_idle()
        self.desenhar()
        
    def get(self, key, no: Node = None):
        if self.isEmpty():
            return False
        
        if no == None: no = self.raiz

        if key == no.key:
            no.estilo['cor'] = VERDE
            self.desenhar()
            
            return True

        else:
            no.estilo['cor'] = AMARELO
            self.desenhar()
            
            if no.left and key < no.key:
                return self.get(key, no.left)
            
            elif no.right and key > no.key:
                return self.get(key, no.right)

        return False

    def get_input(self, evento):
        self.limpar_estilos()
        try:
            key = int(self.textbox.text)

            res = self.get(key)

            self.textbox.set_val("")

            if res:
                self.mensagem.set_text(f"{key} pôde ser encontrado")
    
            else:
                self.mensagem.set_text(f"{key} não pôde ser encontrado")
    
        except ValueError:
            self.mensagem.set_text("Digite um número inteiro válido!")

        self.fig.canvas.draw_idle()
        self.desenhar()

    def profundidade(self, key, no: Node = None):
        if self.isEmpty():
            return -1
        
        if no == None: no = self.raiz

        if key == no.key:
            no.estilo['cor'] = VERDE
            self.desenhar()
            return 0

        elif no.left and key < no.key:
            no.estilo['cor'] = AMARELO
            self.desenhar()
            prof = self.profundidade(key, no.left)
            if prof == -1: return prof
            return 1 + prof

        elif no.right:
            no.estilo['cor'] = AMARELO
            self.desenhar()
            prof = self.profundidade(key, no.right)
            if prof == -1: return prof
            return 1 + prof

        return -1
    
    def profundidade_input(self, evento):
        self.limpar_estilos()
        try:
            key = int(self.textbox.text)

            res = self.profundidade(key)

            self.textbox.set_val("")

            if res == -1:
                self.mensagem.set_text(f"{key} não pôde ser encontrado")
    
            else:
                self.mensagem.set_text(f"A profundidade de {key} é {res}")

        except ValueError:
            self.mensagem.set_text("Digite um número inteiro válido!")

        self.fig.canvas.draw_idle()
        self.desenhar()

    def tamanho(self, no: Node = None):
        if self.isEmpty():
            return 0
        
        if no == None: no = self.raiz
        tam_esq = 0
        tam_dir = 0

        no.estilo['cor'] = VERDE
        self.desenhar()
        
        if no.left:
            tam_esq = self.tamanho(no.left)

        if no.right:
            tam_dir = self.tamanho(no.right)
            
        return 1 + tam_esq + tam_dir

    def tamanho_input(self, evento):
        self.limpar_estilos()
        tam = self.tamanho()

        self.mensagem.set_text(f"O tamanho da árvore é de {tam} nós")
        self.desenhar()

    def height(self, no: Node = None, desenhar = True):
        if self.isEmpty():
            return 0
        
        height_dir = -1
        height_esq = -1

        if no == None: no = self.raiz

        if desenhar:
            no.estilo['cor'] = VERDE
            self.desenhar()

        if no.left:
            height_esq = self.height(no.left, desenhar)

        if no.right:
            height_dir = self.height(no.right, desenhar)

        return 1 + max(height_esq, height_dir)

    def height_input(self, evento):
        self.limpar_estilos()
        res = self.height()

        self.mensagem.set_text(f"A altura da árvore é de {res}")
        self.desenhar()

    def pre_ordem(self, no: Node = None):
        if self.isEmpty():
            return
        
        if no == None: no = self.raiz

        no.estilo['cor'] = VERDE
        #self.desenhar()
        
        self.mensagem.set_text(self.mensagem.get_text() + f"{no.key} ")

        if no.left or no.right:
            no.estilo['contorno'] = VERMELHO
            self.desenhar()

            if no.left:
                self.pre_ordem(no.left)

            if no.right:
                self.pre_ordem(no.right)

        no.estilo['contorno'] = CONTORNO_NORMAL
        self.desenhar()

    def em_ordem(self, no: Node = None):
        if self.isEmpty():
            return

        if no == None: no = self.raiz
        
        if no.left:
            no.estilo['contorno'] = VERMELHO
            self.desenhar()
            self.em_ordem(no.left)

        no.estilo['contorno'] = CONTORNO_NORMAL
        no.estilo['cor'] = VERDE
        
        self.mensagem.set_text(self.mensagem.get_text() + f"{no.key} ")
        self.desenhar()

        if no.right:
            self.em_ordem(no.right)
            
    def pos_ordem(self, no: Node = None):
        if self.isEmpty():
            return
        
        if no == None: no = self.raiz

        if no.left or no.right:
            no.estilo['contorno'] = VERMELHO
            self.desenhar()

            if no.left:
                self.pos_ordem(no.left)

            if no.right:
                self.pos_ordem(no.right)

        no.estilo['contorno'] = CONTORNO_NORMAL
        no.estilo['cor'] = VERDE
    
        self.mensagem.set_text(self.mensagem.get_text() + f"{no.key} ")
        self.desenhar()

    def por_niveis(self, no=None, nivel=0):
        if self.isEmpty():
            return

        if no is None:
            no = self.raiz

        if nivel == 0:
            no.estilo['cor'] = VERDE

            self.mensagem.set_text(
                self.mensagem.get_text() + f"{no.key} "
            )

            self.desenhar()

        else:
            if no.left:
                self.por_niveis(no.left, nivel - 1)

            if no.right:
                self.por_niveis(no.right, nivel - 1)
                
    def percorrer_niveis(self):
        if self.isEmpty():
            return

        altura = self.height(desenhar=False)

        for nivel in range(altura + 1):
            self.por_niveis(self.raiz, nivel)

    def pre_ordem_input(self, evento):
        self.limpar_estilos()
        if self.isEmpty():
            self.mensagem.set_text('A árvore está vazia')
        else:
            self.mensagem.set_text('Pré-ordem: ')
            self.pre_ordem()

        self.desenhar()
        #self.mensagem.set_text('Digite um valor e escolha uma operação')

    def em_ordem_input(self, evento):
        self.limpar_estilos()
        if self.isEmpty():
            self.mensagem.set_text('A árvore está vazia')
        else:
            self.mensagem.set_text('Em-ordem: ')
            self.em_ordem()

        self.desenhar()
        #self.mensagem.set_text('Digite um valor e escolha uma operação')

    def pos_ordem_input(self, evento):
        self.limpar_estilos()
        if self.isEmpty():
            self.mensagem.set_text('A árvore está vazia')
        else:
            self.mensagem.set_text('Pós-ordem: ')
            self.pos_ordem()
                    
        self.desenhar()
        #self.mensagem.set_text('Digite um valor e escolha uma operação')

    def por_niveis_input(self, evento):
        self.limpar_estilos()
        if self.isEmpty():
            self.mensagem.set_text('A árvore está vazia')
        else:
            self.mensagem.set_text('Por niveis: ')
            self.percorrer_niveis()
                    
        self.desenhar()

    def maiorValor(self, no: Node = None):
        if self.isEmpty():
            return
        
        if no == None: no = self.raiz

        if no.right == None:
            no.estilo['cor'] = VERDE
            self.desenhar()
            return no.key
        
        else:
            no.estilo['cor'] = AMARELO
            self.desenhar()
            return self.maiorValor(no.right)

    def maiorValor_input(self, event):
        self.limpar_estilos()
        res = self.maiorValor()
        if res != None:
            self.mensagem.set_text(f'O maior valor é {res}')
        else:
            self.mensagem.set_text(f'A árvore está vazia')
        self.desenhar()

    def menorValor(self, no: Node = None):
        if self.isEmpty():
            return
        
        if no == None: no = self.raiz

        if no.left == None:
            no.estilo['cor'] = VERDE
            self.desenhar()
            return no.key
        
        else:
            no.estilo['cor'] = AMARELO
            self.desenhar()
            return self.menorValor(no.left)

    def menorValor_input(self, event):
        self.limpar_estilos()
        res = self.menorValor()
        if res != None:
            self.mensagem.set_text(f'O menor valor é {res}')
        else:
            self.mensagem.set_text(f'A árvore está vazia')
            
        self.desenhar()

    def comprimento(self, raiz, nivel=0):
        if raiz is None:
            return 0

        return (nivel +
                self.comprimento(raiz.left, nivel + 1) +
                self.comprimento(raiz.right, nivel + 1))

    def comprimento_interno_input(self, evento):
        self.limpar_estilos()
        res = self.comprimento(self.raiz)
        
        self.mensagem.set_text(f'O comprimento interno é de {res}')
          
        self.desenhar()

    def balanceada(self, no: Node = None):
        if self.isEmpty():
            return True

        if no is None:
            no = self.raiz

        altura_esq = -1
        altura_dir = -1

        if no.left:
            altura_esq = self.height(no.left, desenhar=False)

        if no.right:
            altura_dir = self.height(no.right, desenhar=False)

        if abs(altura_esq - altura_dir) > 1:
            return False

        if no.left and not self.balanceada(no.left):
            return False

        if no.right and not self.balanceada(no.right):
            return False

        return True

    def balanceada_input(self, evento):
        self.limpar_estilos()
        res = self.balanceada(self.raiz)

        if not res:
            self.mensagem.set_text(f'A árvore não está balanceada')
        else:
            self.mensagem.set_text(f'A árvore está balanceada')
            
        self.desenhar()

    def desenhar(self, pausas=True):
        self.ax.clear()

        def desenhar_recursivo(no, x, y, deslocamento):
            if no is None:
                return

            cor = no.estilo['cor']
            contorno = no.estilo['contorno']
            width = 1 if contorno == CONTORNO_NORMAL else 3

            self.ax.scatter(x, y, s=1000, color=cor, edgecolors=contorno, zorder=2, linewidths=width)

            self.ax.text(x, y, str(no.key), ha="center", va="center", fontsize=11, zorder=3, weight="bold")

            if no.left:
                self.ax.plot([x, x - deslocamento], [y, y - 1], color="black", zorder=1)

                desenhar_recursivo(no.left, x - deslocamento, y - 1, deslocamento / 2)

            if no.right:
                self.ax.plot([x, x + deslocamento], [y, y - 1], color="black", zorder=1)

                desenhar_recursivo(no.right, x + deslocamento, y - 1, deslocamento / 2)

        if self.raiz:
            desenhar_recursivo(self.raiz, 0, 0, 4)
    
        self.ax.set_title("Árvore Binária de Busca", fontsize=16)

        self.ax.axis("off")

        if pausas:
            plt.pause(0.4)

        self.fig.canvas.draw_idle()
        if pausas:
            self.fig.canvas.flush_events()

    def isEmpty(self):
        return self.raiz == None

    def limpar_estilos(self, no: Node = None):
        if self.isEmpty():
            return
        
        if no == None: no = self.raiz

        #travessia pré-ordem
        self.limpar_estilo(no)

        if no.left:
            self.limpar_estilos(no.left)

        if no.right:
            self.limpar_estilos(no.right)

arvore = BST()

plt.show()