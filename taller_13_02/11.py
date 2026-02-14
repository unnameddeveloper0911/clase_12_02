#Write a function that finds and returns all duplicates in a list of numbers.

lista=[1,2,3,4]

def duplicar(lista):
    duplicados=[]
    numero=0
    for i in range(len(lista)):
        numero=lista[i]*2
        duplicados.append(numero)
    return duplicados

print("La lista de duplicados es: ", duplicar(lista))