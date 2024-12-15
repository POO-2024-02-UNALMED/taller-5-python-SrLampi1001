class Zona:
    
    def __init__(self, nombre = '', zoo = None, animales = None):
        self.__nombre = nombre
        self.__zoo = zoo
        self.__animales = animales
    def getZoo(self):
        return self.__zoo
    def setZoo(self,zoo):
        self.__zoo = zoo
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre =nombre
    def __str__(self):
        return self.__nombre
    def agregarAnimales(self, animal):
        if self.__animales==None:
            self.__animales = []
        self.__animales.append(animal)
    def getAnimales(self):
        return self.__animales
    def cantidadAnimales(self):
        return len(self.__animales)
    
    