from zooAnimales.animal import Animal
class Anfibio(Animal):
    __listado = None
    ranas = 0
    salamandras = 0
    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', colorPiel = '', venenoso = False):
        super().__init__(nombre, edad, habitat, genero, None)
        self.__colorPiel = colorPiel
        self.__venenoso = venenoso
    def isVenenoso(self):
        return self.__venenoso
    def setVenenoso(self, bool):
        self.__venenoso = bool
    def getColorPiel(self):
        return self.__colorPiel
    def setColorPiel(self, color):
        self.__colorPiel = color
    def movimiento(self):
        return 'saltar'
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        new= Anfibio(nombre, edad, 'selva', genero, "rojo", True)
        Anfibio.putListado(new)
        return new
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        new = Anfibio(nombre, edad, 'selva', genero, "negro y amarillo", False)
        Anfibio.putListado(new)
        return new
    @classmethod
    def putListado(cls, obj):
        if cls.__listado == None:
            cls.__listado = []
        cls.__listado.append(obj)
    @classmethod
    def cantidadAnfibios(cls):
        if cls.__listado == None:
            return 0
        else:
            return len(cls.__listado)