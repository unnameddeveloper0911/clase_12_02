class Nodo:
    def __init__ (self, valor = None):
        self._valor=valor
        self._siguiente=None
        
    @property
    def valor(self):
        return self._valor
    
    
    @property
    def siguiente(self):
        return self._siguiente
    
    @valor.setter
    def valor(self, valor):
        self._valor=valor
        
    @siguiente.setter
    def siguiente (self, siguiente):
        self._siguiente=siguiente
        
    