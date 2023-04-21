class Papaya:

    def __init__(self):
        self.__nombre=None
        self.__cantidad=None
        self.__estado=None
        self.__precio=None
    
    #GETTERS (PARA SACAR INFORMACION/MOSTRANDO)
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def precio(self):
        return self.__precio
    
    
    #SETTERS (PARA INGRESAR INFORMACION/GUARDANDO)
    
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato
        
    @cantidad.setter
    def cantidad(self,dato):
        self.__cantidad=dato
    
    @estado.setter
    def estado(self,dato):
        self.__estado=dato
        
    @precio.setter
    def precio(self,dato):
        self.__precio=dato
    
    def describirFruta(self):
        print(f'mi fruta papaya es medio maluca y medio rica... pruebala!!!')
        
    