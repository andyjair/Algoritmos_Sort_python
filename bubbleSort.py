def bubbleSort(lista):
    #import pdb; pdb.set_trace()
    n = len(lista)
    for i in range (1, n):
        for j in range (0, n-1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

lista = [5,4,1,8,3,7,2,6,9]

if __name__=="__main__":
    print(lista)
    print(bubbleSort(lista))    
     