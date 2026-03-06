from lista_simple import ListaSimple

if __name__ == "__main__":
    lista_simple=ListaSimple()
    lista_simple.agregar_al_final(1)
    lista_simple.agregar_al_final(2)
    lista_simple.agregar_al_final(3)
    puntero = lista_simple.cabeza
    
    while puntero is not None:
        print(puntero.valor)
        puntero = puntero.siguiente
        
        
        