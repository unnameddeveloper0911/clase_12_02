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
            if self._cabeza is None:
                self._cabeza=Nodo(valor)
            else:
                pass
                
