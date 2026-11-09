from fila_prioridade_array import *

fila_p = FilaArray()
fila_n = FilaArray()
menu = '''-------------------------
1. Chegada de pessoa para atendimento
2. Realizar atendimento
3. Listar pessoas na fila
4. Sair
-------------------------
Opção: '''

atender_prioridade = False
atendidos = 0
atendidos_prioridade = 0 
while True:
    opcao = input(menu)
    print()
    if opcao == '1':
        nome = input("Indique o nome da pessoa: ")
        
        if "*" in nome:
            prioridade = True
        else:
            prioridade = False
                
        if prioridade:
            fila_p.enqueue(PessoaNaFila(nome))
        else:
            fila_n.enqueue(PessoaNaFila(nome))
            
    if opcao == '2':  # Dequeue de acordo com a política 2 sem 1 com
        # Verifica se as duas filas estão vazias
        if fila_p.isEmpty() and fila_n.isEmpty():
            print("Não há pessoas na fila para atendimento.")

        # A cada 3 atendimentos, tenta atender prioridade
        elif atendidos % 3 == 2:

            if not fila_p.isEmpty():
                print(f"Atendendo pessoa com prioridade: {fila_p.dequeue()}")
                atendidos += 1
                atendidos_prioridade += 1

            elif not fila_n.isEmpty():
                print(f"Fila de prioridade vazia.")
                print(f"Atendendo pessoa sem prioridade: {fila_n.dequeue()}")
                atendidos += 1

        # Nos outros dois atendimentos, tenta atender sem prioridade
        else:

            if not fila_n.isEmpty():
                print(f"Atendendo pessoa sem prioridade: {fila_n.dequeue()}")
                atendidos += 1

            elif not fila_p.isEmpty():
                print(f"Fila sem prioridade vazia.")
                print(f"Atendendo pessoa com prioridade: {fila_p.dequeue()}")
                atendidos += 1
                atendidos_prioridade += 1

    if opcao == '3': 
        print("Pessoas com prioridade:")
        fila_p.PrintLista()
        print("Pessoas sem prioridade:")
        fila_n.PrintLista()

    if opcao == '4':
        if fila_p.isEmpty() and fila_n.isEmpty():
            print (f"Total de pessoas atendidas: {atendidos}")
            if atendidos > 0:
                percentual_prioridade = (atendidos_prioridade / atendidos) * 100
                percentual_sem_prioridade = 100 - percentual_prioridade
                print(f"Percentual de atendimentos com prioridade: {percentual_prioridade:.2f}%")
                print(f"Percentual de atendimentos sem prioridade: {percentual_sem_prioridade:.2f}%")
            break
        else:
            print("Ainda existem pessoas na fila. Não é possível sair.")
        
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida. Por favor, tente novamente.")