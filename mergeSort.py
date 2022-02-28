def merge(lista1, lista2):
    lista3 = []
    while len(lista1)>0 and len(lista2)>0:
        if lista1[0]< lista2[0]:
            lista3.append(lista1[0])
            lista1 = lista1[1:]
        else:
            lista3.append(lista2[0])
            lista2 = lista2[1:]
    if len(lista1)>0:
        lista3 = lista3 + lista1 
    if len(lista2)>0:
        lista3 = lista3 + lista2
    return lista3                      

def mergeSort(lista):
    if len(lista) == 1:
        return lista
    listaIzq = lista[:len(lista)//2]
    listaDer = lista[len(lista)//2:]
    listaIzq = mergeSort(listaIzq)
    listaDer = mergeSort(listaDer) 
    return merge(listaIzq, listaDer)   

lista = [5,4,1,8,3,7,2,6,9]

if __name__=="__main__":
    print(lista)
    print(mergeSort(lista))