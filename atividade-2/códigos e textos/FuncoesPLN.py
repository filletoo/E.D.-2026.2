import re
import matplotlib.pyplot as plt

def lerOpcao():
    escolha = " "
    while escolha not in "123456":
        escolha = input('''----------------------------------------------------------------
1 - Mostrar quantidade de palavras
2 - Remover stopwords e mostrar dados estatísticos
3 - Mostrar top(k) palavras mais frequentes
4 - Imprimir Hapaxes Legomenons
5 - Mostrar o gráfico com a Curva de Zipf e os cortes de Luhn
6 - Sair
----------------------------------------------------------------
Escolha uma opcao: ''')
        
        if escolha not in "123456":
            print("Escolha uma opcao valida") 

    return escolha

def separar_texto(texto):
    palavras = re.split(r'[,.;:!?()—•...*&"\n ]+', texto)
    palavras = [i.lower() for i in palavras]
    return palavras

def separar_stopwords(palavras, stopwords):
    palavras_sem_stopwords = []
    so_stopwords = []
    for p in palavras:
        if p not in stopwords:
            palavras_sem_stopwords.append(p)
        else:
            so_stopwords.append(p)
    return palavras_sem_stopwords, so_stopwords

def pegar_frequencia(palavras):
    frequencia = dict()
    for p in palavras:
        if p not in frequencia: frequencia[p] = 1
        else: frequencia[p] += 1

    return frequencia

def top(k, frequencia):
    maiores_freq = []
    p_mais_freq = dict()
    for i in frequencia:
        maiores_freq.append(frequencia[i])

    maiores_freq.sort(reverse=True)
    n = k
    for i in range(k, len(maiores_freq)):
        if maiores_freq[i] == maiores_freq[k - 1]:
            n += 1
        else: break

    maiores_freq = maiores_freq[0:n]
    for i in maiores_freq:
        for j in frequencia:
            if frequencia[j] == i:
                p_mais_freq[j] = i

    return p_mais_freq
     
def hapaxes_legomenons(palavras):
    frequencia  = pegar_frequencia(palavras)
    hl = []
    for i in frequencia:
        if frequencia[i] == 1:
            hl.append(i)

    return hl