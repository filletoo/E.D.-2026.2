from pilha_lista_encadeada import *

atras = PilhaLista()
frente = PilhaLista()
menu = '''-----------------
1. Voltar
2. Avançar
3. Abrir nova URL
4. Exibir URL atual
5. Sair
-----------------
Opcao: '''

url_atual = "google.com"

while True:
    opcao = input(menu)
    print()
    if opcao == '1':
        aux = atras.pop()
        if aux != None:
            frente.push(url_atual)
            url_atual = aux
            print(f"URL atual: {url_atual}")
        else: 
            print("Não há mais páginas para voltar no histórico")

    elif opcao == '2':
        aux = frente.pop()
        if aux != None:
            atras.push(url_atual)
            url_atual = aux
            print(f"URL atual: {url_atual}")
            
        else:
            print("Não há páginas para avançar")

    elif opcao == '3':
        atras.push(url_atual)
        aux = frente.top
        while aux != None:
            aux = frente.pop()

        url_atual = input("Nova URL:\n")

    elif opcao == '4':
        print(f"URL atual: {url_atual}")

    elif opcao == '5':
        break

    else:
        print("Escolha uma opção válida")