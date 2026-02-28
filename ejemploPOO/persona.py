class Persona:
    
    #Eqiuvalente de un construtor con parametros
    def __init__(self, nombre, edad):
        #Atributos
        self._nombre=nombre
        self._edad=edad
    
    #Equivalentes de los Getters
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    #Setters    
    @nombre.setter
    def nombre (self,nombre):
        self._nombre=nombre
    
    @edad.setter
    def edad (self, edad):
        self._edad=edad
        
    
    def saludar(self):
        return f"Hola, mi nombre es {self._nombre} y tengo {self._edad} años. :)"
    