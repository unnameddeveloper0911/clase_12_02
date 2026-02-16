##Return the second element of the given list. If the list has no second element, return None.
lista = []

def datos(lista):
    cant = int(input("ingrese la cantidad de datos: "))
    for i in range(cant):
        lista.append(input("ingrese un dato"))
        
def segDato(lista):
    try:
        if len(lista)<1: ## si hay menos de 2 datos, no retorna nada
            return None
        else: print("el segundo dato es: " + lista[1])
    except IndexError:
        print(" ")

datos(lista)
segDato(lista)
    