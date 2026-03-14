from nodo import Nodo
class ListaDoble:
    def __init__(self): 
        
        self._cabeza=None
        self._cola=None
        
    @property
    def cabeza (self):
        return self._cabeza
            
    @property
    def cola (self):
        return self._cola
    
    @cabeza.setter
    def cabeza (self, cabeza):
        self._cabeza=cabeza
    
    @cola.setter
    def cola (self, cola):
        self._cola=cola            
            
    def agregar(self, valor):
        nodo=Nodo(valor)
        if self._cabeza is None:
            self._cabeza=nodo
        else:
            puntero=self._cabeza
            while (puntero.siguiente is not None):
                puntero=puntero.siguiente
            puntero.siguiente=nodo        
    
    def agregar_al_inicio(self, valor):
        nodo=Nodo(valor)
        if self._cabeza is None:
            self._cola=nodo
            self._cabeza=nodo
        else:
            aux=self._cabeza
            self._cabeza.anterior=nodo
            self._cabeza=self._cabeza.anterior
            self._cabeza.siguiente=aux