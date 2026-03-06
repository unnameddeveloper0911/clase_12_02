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