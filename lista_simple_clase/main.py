from lista_simple import ListaSimple

if __name__ == "__main__":
    lista_simple=ListaSimple()

    lista_simple.agregar_al_final(5)
    lista_simple.agregar_al_final(4)
    lista_simple.agregar_al_final(3)
    lista_simple.agregar_al_final(2)
    lista_simple.agregar_al_final(1)
    
    print("Imprimir lista")
    puntero = lista_simple.cabeza
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente
        
    print("")
    print("Imprimir lista ordenada")
    
    puntero=lista_simple.cabeza
    lista_simple.bubble_sort()
    while puntero is not None:
        print(puntero.valor)
        puntero=puntero.siguiente
        
    print("")
    
    print("Imprimir lista con nodo eliminado")
    puntero = lista_simple.cabeza
    lista_simple.metodo_clean(1)
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente
            
    
        
    print("")
    print("Imprimir lista con nodo insertado")
    lista_simple.metodo_insertar(0,7)
    puntero = lista_simple.cabeza
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente 
    
    
            
        
    