def heapify(lista, i):
    if 2 * i + 2 <= len(lista) - 1:
        if lista[2 * i + 1] <= lista[2 * i + 2]:
            min = 2 * i + 1
        else:
            min = 2 * i + 2
        if lista[i] >lista[min]:
            aux = lista[i]
            lista[i] = lista[min]
            lista[min] = aux
            heapify(lista, min)
    elif 2 * i + 1 <= len(lista) - 1:
        if lista[i] > lista[2 * i + 1]:
            aux = lista[i]
            lista[i] = lista[2*i+1]
            lista[2 * i + 1] = aux
    return lista                     

def headSort(lista):
    lista2 = []
    for i in range(len(lista)//2-1,-1,-1):
        lista = heapify(lista, i)
    for i in range(0, len(lista)):
        aux = lista[0]
        lista[0] = lista[len(lista) - 1]
        lista[len(lista) - 1] = aux
        lista2.append(aux)
        lista = lista[:len(lista) - 1]
        lista = heapify(lista, 0)
    return lista2            
 
lista = [20,15,13,10,34,25,31,28,12]

if  __name__=="__main__":
    print(lista)
    print(headSort(lista))