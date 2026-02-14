#Write a program that finds the largest and smallest number in a given list of numbers.

lista=[1,2,3,4,5]

def mayor(lista):
    mayor=lista[0]
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def menor(lista):
    menor=lista[0]
    for i in lista:
        if i<menor:
            menor=i
    return menor

print("El numero mayor es: ", mayor(lista))
print("El numero menor es: ", menor(lista))