from FuncoesPLN import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
    caminho = "C:\\Users\\carlo\\OneDrive\\Documentos\\Faculdade\\Estrutura de Dados\\atividade 2\\"
    with open(caminho + "texto.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    with open(caminho + "stopwords.txt", "r", encoding = "utf-8") as s:
        stopwords = s.read().split()

    palavras = separar_texto(texto)
    opcao2 = False
    opcao3 = False
    while (True):
        escolha = lerOpcao()
        
        if escolha == "1":
            print("Quantidade de palavras no texto:", len(palavras))

        elif escolha == "2":
            palavras_sem_stopwords, so_stopwords = separar_stopwords(palavras, stopwords)
            print("#palavrasOriginais:", len(palavras))
            print(f"#stopwords: {len(so_stopwords)}\n%stopwords: %{100*round(len(so_stopwords)/len(palavras), 2)}")
            print(f"#palavrasSemStopwords: {len(palavras_sem_stopwords)}\n%palavrasSemStopwords: %{100*round(len(palavras_sem_stopwords)/len(palavras), 2)}")
            opcao2 = True
        elif escolha == "3" and opcao2:
            while True:
                k = int(input("K: "))
                if k <= 0: print("K invalido")
                else: break
            while True:
                o = input("Deseja incluir as stopwords?:\n1 - Sim\n2 - Nao\n")
                if o != '1' and o != '2': print("Escolha invalida")
                else: break
            if o == '1':
                frequencia = pegar_frequencia(palavras)
            else:
                frequencia = pegar_frequencia(palavras_sem_stopwords)
            p_mais_freq = top(k, frequencia)
            n = 1
            for i in p_mais_freq:
                print(f"#{n} = {i} (frequencia: {p_mais_freq[i]})")
                n += 1
            opcao3 = True
        elif escolha == "4":
            hl = hapaxes_legomenons(palavras)
            print("Palavras de frequencia unica: ")
            print(hl)
            
        elif escolha == "5" and opcao3:
            frequencia = pegar_frequencia(palavras)
            plt.figure(figsize=(1366, 728, 'px'))
            frequencia_sortida = sorted(frequencia, key=lambda x: frequencia[x], reverse=True)
            plt.plot([i for i in frequencia_sortida], [frequencia[i] for i in frequencia_sortida])
            plt.axvline(x=len(set(so_stopwords)), color='green', linestyle='--', label='Primeiro Corte')
            hl = hapaxes_legomenons(palavras)
            plt.axvline(x=len(frequencia_sortida)-len(hl), color='red', linestyle='--', label='Segundo Corte')
            plt.ylabel("Frequencia")
            plt.xlabel("Palavras")
            plt.xticks(list(range(0, len(frequencia_sortida), 10)),rotation=90)
            plt.show()
        elif escolha == "6":
            break
        elif escolha in "123456":
            print("Faça as escolhas em ordem")
        