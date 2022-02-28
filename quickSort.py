def quickSort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista.pop()
    lista1 = []
    lista2 = []
    for e in lista:
        if e <= pivote:
            lista1.append(e)
        else:
            lista2.append(e)
    lista1 = quickSort(lista1)
    lista2 = quickSort(lista2)
    return lista1 + [pivote] + lista2 

lista = [15,25,10,35,24,17,11,26]

if __name__=="__main__":
    print(lista)
    print(quickSort(lista))