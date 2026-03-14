class Nodo:
    def __init__(self, valor=None):
        self._valor=valor
        self._siguiente=None
        self._anterior=None
        
    @property
    def valor(self):
        return self._valor
        
    @property
    def siguiente(self):
        return self._siguiente
        
    @property
    def anterior(self):
        return self._anterior
    
    @valor.setter
    def valor(self, valor):
        self._valor=valor
            
    @siguiente.setter
    def siguiente(self, siguiente):
        self._siguiente=siguiente
            
    @anterior.setter
    def anterior(self, anterior):
        self._anterior=anterior
    
    
            
        