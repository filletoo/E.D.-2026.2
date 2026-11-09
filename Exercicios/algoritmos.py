import random

def is_sorted(array, reverse=False):
    for i in range(len(array) - 1):
        if not reverse:
            if array[i] > array[i + 1]:
                return False
        else:
            if array[i] < array[i + 1]:
                return False

    return True

def lista_random(inicio = 0, fim = 1000, quant = 20):
    lista = random.choices(range(inicio, fim + 1), k=random.randint(0, quant))
    return lista

def tem_repetido(array):
    return len(set(array)) != len(array)

#bubble sort
def bubble_sort(array):
    ordenado = False
    ultimo = len(array)
    while not ordenado:
        ordenado = True
        for i in range(ultimo - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                ordenado = False
        ultimo -= 1
    return array

#selection sort
def selection_sort(array):
    inicio = 0
    while inicio < len(array):
        menor = inicio
        for i in range(inicio + 1, len(array)):
            if array[i] < array[menor]:
                menor = i

        array[inicio], array[menor] = array[menor], array[inicio]
        inicio += 1

#inserstion sort
def insertion_sort(array):
    copia = [None] * len(array)
    quant_copia = 0

    for i in range(len(array)):
        item = array[i]
        j = 0
        for j in range(quant_copia - 1, -1, -1):
            if copia[j] > item:
                copia[j + 1] = copia[j]
            else:
                j += 1
                break

        copia[j] = item
        quant_copia += 1

    return copia

#shell sort
def shell_sort(array):
    gap = len(array)//2

    while gap > 0:
        for i in range(len(array)):
            trocou = False
            if i + gap < len(array) and array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                trocou = True

            while trocou and i - gap >= 0:
                trocou = False
                if array[i - gap] > array[i]:
                    array[i], array[i - gap] = array[i - gap], array[i]
                    trocou = True

                i = i - gap

        gap //= 2

#merge sort (terminar)
def merge_sort(array, inicio = 0, fim = None):
    
    if fim == None: fim = len(array) - 1

    if len(array[inicio:fim + 1]) <= 1:
        return

    if len(array[inicio:fim + 1]) == 2:
        if array[inicio] > array[fim]:
            array[inicio], array[fim] = array[fim], array[inicio]

        return 
    
    meio = (inicio + fim)//2

    merge_sort(array, inicio, meio)
    merge_sort(array, meio + 1, fim)
    
    i = inicio
    j = meio + 1
    pos = 0

    copia = array[inicio:fim + 1]
    while i <= meio and j <= fim:
        if array[i] < array[j]:
            copia[pos] = array[i]
            i += 1
        else:
            copia[pos] = array[j]
            j += 1

        pos += 1

    while i <= meio:
        copia[pos] = array[i]
        pos += 1
        i += 1

    while j <= fim:
        copia[pos] = array[j]
        pos += 1
        j += 1

    array[inicio: fim + 1] = copia

#quick sort
def quick_sort(array):
    pivo = 0

    while pivo < len(array):
        #print(array)
        #print(array[pivo])
        i = pivo + 1
        j = len(array) - 1

        #trocou = False
        while i <= j:
            if array[i] >= array[pivo] and array[j] < array[pivo]:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
                #trocou = True
            else:
                if array[i] < array[pivo]:
                    i += 1
                if array[j] >= array[pivo]:
                    j -= 1

        if j == pivo:
            pivo += 1
        else:    
            array[pivo], array[j] = array[j], array[pivo]
           
#heap sort
def no_esq(i):
    return 2*i + 1

def no_dir(i):
    return 2*i + 2

def no_pai(i):
    if (i - 2) % 2 == 0:
        return (i - 2) // 2

    elif (i - 1) % 2 == 0:
        return (i - 1) // 2

    return -1

def heap_sort(array):
    final = len(array) - 1
    operacoes = 0
    while final > 0:
        for i in range(final, -1, -1):
            atual = i
            while True:
                maior = atual

                esq = no_esq(atual)
                dir = no_dir(atual)

                if esq <= final and array[esq] > array[maior]:
                    maior = esq

                if dir <= final and array[dir] > array[maior]:
                    maior = dir

                if array[maior] != array[atual]:
                    array[maior], array[atual] = array[atual], array[maior]
                    atual = maior
                    operacoes += 1
                    
                else:
                    break

        array[0], array[final] = array[final], array[0]
        final -= 1

    return operacoes

if __name__ == '__main__':
    for i in range(5):
        lista = lista_random(quant=200)
        print("inicial:", lista)

        #bubble_sort(lista)
        #selection_sort(lista)
        #lista = insertion_sort(lista)
        #shell_sort(lista)
        quick_sort(lista)
        #merge_sort(lista)
        #operacoes = heap_sort(lista)
        print("ordenado:", lista)
        #print("repetido: ", tem_repetido(lista))
        #print("i:", i, ", operacoes:", operacoes)
        print(is_sorted(lista))
        if is_sorted(lista) == False:
            print("deu errado")
            break
        
        #print("repetido: ", tem_repetido(lista))

        i *= 2

    print("deu certo")