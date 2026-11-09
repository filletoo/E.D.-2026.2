import random
import time

class Carta:
    def __init__(self, naipe, valor, simbolo):
        self.naipe = naipe
        self.valor = valor
        self.simb = simbolo
        self.escondida = False
        if self.naipe == "paus" or self.naipe == "espadas":
            self.cor = "preto"
        else:
            self.cor = "vermelho"
   
class Baralho:
    simbolos = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "W"]
    def __init__(self, A=1, J=11, Q=12, W=13):
        self.cartas = []
        self.pos = 0
        for i in range(4):
            if i == 0: naipe = "paus"
            elif i == 1: naipe = "ouros"
            elif i == 2: naipe = "espadas"
            elif i == 3: naipe = "copas"
            for simb in self.simbolos:
                if simb == "A":
                    valor = A
                elif simb == "J":
                    valor = J
                elif simb == "Q":
                    valor = Q
                elif simb == "W":
                    valor = W
                else:
                    valor = int(simb)
                self.cartas.append(Carta(naipe, valor, simb))

    def embaralhar(self):
        random.shuffle(self.cartas)

    def pedir(self, mao):
        mao.append(self.cartas[baralho.pos])
        self.pos += 1

def somar_cartas(mao):
    soma = 0
    for carta in mao:
        soma += carta.valor

    for carta in mao:
        if soma <= 21: 
            break
        if carta.simb == "A":
            soma -= carta.valor
            soma += 1

    return soma

def imprimir_cartas(mao):
    soma = somar_cartas(mao)
    
    for i in mao:
        if i.escondida == False:
            print(i.simb, end=" ")
        else:
            print("X", end= " ")
            soma = "?"
    print(f"+{soma}")

def imprimir_tudo(mao1, mao2):
    print("Banca:   ", end="")
    imprimir_cartas(mao1)
    print("Jogador: ", end="")
    imprimir_cartas(mao2)
    print()

if __name__ == "__main__":
    escolha = 's'
    saldo = 100.0
    print(f"Saldo: {saldo}")
    while escolha == 's' and saldo > 0:
        escolha = ""
        baralho = Baralho(A=11, J=10, Q=10, W=10)
        soma_jogador = 0
        mao_jogador = []
        soma_banca = 0
        mao_banca = []
        baralho.embaralhar()
        jogador_ganhou = -1
        desistiu = False
        menu = "---------------\n1 - Pedir\n2 - Parar\n3 - Dobrar Aposta\n4 - Desistir\n---------------\n"

        aposta = 0
        while aposta > saldo or aposta == 0:
            aposta = float(input("Defina a aposta inicial: R$"))
            if saldo - aposta < 0:
                print("Dinheiro insuficiente para esta aposta.")

        for i in range(2):
            baralho.pedir(mao_jogador)
            baralho.pedir(mao_banca)
        mao_banca[1].escondida = True

        soma_banca = somar_cartas(mao_banca)
        soma_jogador = somar_cartas(mao_jogador)

        if soma_jogador != 21 and soma_banca != 21:
            imprimir_tudo(mao_banca, mao_jogador)
            while soma_jogador < 21:
                jogada = "ç"
                while jogada not in menu  and not jogada.isdigit():
                    
                    jogada = input(menu)
                    if jogada not in menu and not jogada.isdigit():
                        print("Input Inválido")

                if jogada == "1":
                    baralho.pedir(mao_jogador)
                    soma_jogador = somar_cartas(mao_jogador)
                elif jogada == "2":
                    imprimir_tudo(mao_banca, mao_jogador)
                    break

                if len(mao_jogador) <= 2:
                    if jogada == "3":
                        if aposta*2 <= saldo:
                            aposta *= 2
                            baralho.pedir(mao_jogador)
                            soma_jogador = somar_cartas(mao_jogador)
                        else:
                            print("Saldo insuficiente")
                    elif jogada == "4":
                        aposta /= 2
                        desistiu = True
                        break
                else:
                    menu = "---------------\n1 - Pedir\n2 - Parar\n---------------\n"
                
                imprimir_tudo(mao_banca, mao_jogador)

            mao_banca[1].escondida = False

            imprimir_tudo(mao_banca, mao_jogador)
            if not desistiu:
                if soma_jogador == 21:
                    print("Você ganhou!")
                    jogador_ganhou = 1
                elif soma_jogador > 21:
                    print("Voce perdeu!")
                else:
                    while soma_banca < 17:
                        baralho.pedir(mao_banca)
                        soma_banca = somar_cartas(mao_banca)
                        time.sleep(1)

                        imprimir_tudo(mao_banca, mao_jogador)

                    if soma_banca > 21:
                        print("Banca estourou. Voce ganhou!")
                        jogador_ganhou = 1 
                    elif soma_banca == 21:
                        print("Banca ganhou. Você perdeu")
                    elif soma_jogador > soma_banca:
                        print("Voce ganhou")
                        jogador_ganhou = 1
                    elif soma_jogador < soma_banca:
                        print("Você perdeu")
                    else:
                        print("Empate")
                        jogador_ganhou = 0
        else:
            mao_banca[1].escondida = False
            imprimir_tudo(mao_banca, mao_jogador)
            if soma_jogador == 21 and soma_banca == 21:
                print("Empate")
                jogador_ganhou = 0
            elif soma_banca == 21:
                print("Você perdeu!")
            elif soma_jogador == 21:
                print("Jogador ganhou!")
                jogador_ganhou = 1
            
        saldo += jogador_ganhou*aposta
        print(f"Saldo: {saldo}")
        if saldo == 0: 
            print("Saldo insuficiente")
            break
        while escolha != 's' and escolha != 'n':
            escolha = input("Deseja jogar de novo? s/n: ")
            if escolha != 's' and escolha != 'n':
                print("Input inválido")
