from lista_simple import ListaSimple

if __name__ == "__main__":
    lista_simple=ListaSimple()

    lista_simple.agregar_al_final(1)
    lista_simple.agregar_al_final(4)
    lista_simple.agregar_al_final(5)
    lista_simple.agregar_al_final(2)
    lista_simple.agregar_al_final(3)
    
    
    puntero = lista_simple.cabeza
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente
        
    print("")
    
    puntero=lista_simple.cabeza
    lista_simple.bubble_sort()
    while puntero is not None:
        print(puntero.valor)
        puntero=puntero.siguiente
        
    print("")
    
    
    puntero = lista_simple.cabeza
    lista_simple.metodo_clean(3)
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente
        
    
        
    print("")
    
    puntero = lista_simple.cabeza
    lista_simple.metodo_insertar(0,10)
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente
    
    
            
        
    