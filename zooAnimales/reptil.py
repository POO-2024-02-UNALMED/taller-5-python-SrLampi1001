from zooAnimales.animal import Animal

class Reptil(Animal):
    __listado = None
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', colorEscamas = '', largoCola = 0):
        super().__init__(nombre, edad, habitat, genero, None)
        self.__colorEscamas = colorEscamas
        self.__largoCola = largoCola
    def getColorEscamas(self):
        return self.__colorEscamas
    def setColorEscamas(self, color):
        self.__colorEscamas = color
    def getLargoCola(self):
        return self.__largoCola
    def setLargoCola(self, largo):
        self.__largoCola = largo
    def movimiento(self):
        return 'reptar'
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        new= Reptil(nombre, edad, 'humedal', genero, "verde", 3)
        Reptil.putListado(new)
        return new
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        new = Reptil(nombre, edad, 'jungla', genero, "blanco", 1)
        Reptil.putListado(new)
        return new
    @classmethod
    def putListado(cls, obj):
        if cls.__listado == None:
            cls.__listado = []
        cls.__listado.append(obj)
    @classmethod
    def cantidadReptiles(cls):
        if cls.__listado == None:
            return 0
        else:
            return len(cls.__listado)