#Write a function that returns a new list with only the elements that are present in both given lists.

lista1=[1,2,3,4]
lista2=[3,4,5,6]

def comparar(lista1, lista2):
    comunes=[]
    for i in lista1:
        if i in lista2:
            comunes.append(i)
    return comunes

print("Los numeros comunes en ambas listas son: ", comparar(lista1, lista2))