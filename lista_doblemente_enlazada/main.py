from lista_doble import ListaDoble

if __name__=='__main__':
    
    lista=ListaDoble()
    
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.agregar(4)
    
    
    print("Imprimir lista")
    puntero = lista.cabeza
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente
    
    print("Agregar al inicio")
    lista.agregar_al_inicio(5)
    puntero = lista.cabeza
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente