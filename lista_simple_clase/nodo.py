class Nodo:
    def __init__ (self, valor = None):
        self._valor=valor
        self._siguiente=None
        self._borrar=None
        
    @property
    def valor(self):
        return self._valor
    
    
    @property
    def siguiente(self):
        return self._siguiente
    
    @property
    def borrar(self):
        return self._borrar
    
    @valor.setter
    def valor(self, valor):
        self._valor=valor
        
    @siguiente.setter
    def siguiente (self, siguiente):
        self._siguiente=siguiente
        
    @borrar.setter
    def borrar (self, borrar):
        self._borrar=borrar