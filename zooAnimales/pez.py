from zooAnimales.animal import Animal
class Pez(Animal):
    __listado = None
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', colorEscamas = '', cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero, None)
        self.__colorEscamas = colorEscamas
        self.__cantidadAletas = cantidadAletas
    def getColorEscamas(self):
        return self.__colorEscamas
    def setColorEscamas(self, color):
        self.__colorEscamas = color
    def getCantidadAletas(self):
        return self.__cantidadAletas
    def setCantidadAletas(self, cantidad):
        self.__cantidadAletas = cantidad
    def movimiento(self):
        return 'nadar'
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        new= Pez(nombre, edad, 'selva', genero, "rojo", 6)
        Pez.putListado(new)
        return new
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        new = Pez(nombre, edad, 'selva', genero, "gris", 6)
        Pez.putListado(new)
        return new
    @classmethod
    def putListado(cls, obj):
        if cls.__listado == None:
            cls.__listado = []
        cls.__listado.append(obj)
    @classmethod
    def cantidadPeces(cls):
        if cls.__listado == None:
            return 0
        else:
            return len(cls.__listado)