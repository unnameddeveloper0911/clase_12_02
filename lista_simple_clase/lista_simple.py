from nodo import Nodo
class ListaSimple:
    def __init__ (self):
        
        self._cabeza= None
        
    @property
    def cabeza (self):
        return self._cabeza
        
    @cabeza.setter
    def cabeza (self, cabeza):
        self._cabeza=cabeza
             
    def agregar_al_final(self,valor):
        nuevo_nodo=Nodo(valor)
        if self._cabeza is None:
            self._cabeza=nuevo_nodo
        else:
            puntero=self._cabeza
            while (puntero.siguiente is not None):
                puntero=puntero.siguiente
            puntero.siguiente=nuevo_nodo
            
    
    def metodo_clean(self,indice):
        nodo=Nodo(indice)
        aux=self._cabeza.siguiente
        if self._cabeza is None:
            self._cabeza=None
        else:
            puntero=self._cabeza
            contador=0
            while (contador<indice-1):
                puntero=puntero.siguiente
                contador+=1
            aux=puntero.siguiente
            puntero.siguiente=aux.siguiente
            puntero.borrar=indice-1
            # return valor que se borra
            
            
           
    def metodo_insertar(self,indice,valor):
        nodo = Nodo(valor)
        if self._cabeza is None:
            self._cabeza=nodo
        else:
            puntero = self._cabeza
            contador = 0
            while(contador < indice-1):
                puntero = puntero.siguiente
                contador += 1
            aux = puntero.siguiente
            puntero.siguiente = nodo
            nodo.siguiente = aux
    
    def bubble_sort(self):
        if self._cabeza is None:
            self._cabeza=None
        else:
            puntero=self._cabeza
            while (puntero.siguiente is not None):
                while (puntero.siguiente is not None):
                    if puntero.valor>puntero.siguiente.valor:
                        aux=puntero.valor
                        puntero.valor=puntero.siguiente.valor
                        puntero.siguiente.valor=aux
                    puntero=puntero.siguiente
    
    
                    
        
        
        
        