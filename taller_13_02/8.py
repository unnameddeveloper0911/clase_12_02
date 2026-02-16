lista1 = [1,4,6,4,2,3,5,7]
lista2 = [7,8,9,0,6,5,4]
def comunes(lista1, lista2):
    lista3=[]
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                lista3.append(lista1[i])
    return lista3
print(comunes(lista1, lista2))