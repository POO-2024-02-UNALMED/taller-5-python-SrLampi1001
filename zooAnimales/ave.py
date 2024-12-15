from zooAnimales.animal import Animal
class Ave(Animal):
    __listado = None
    halcones = 0
    aguilas = 0
    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', colorPlumas = ''):
        super().__init__(nombre, edad, habitat, genero, None)
        self.__colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self.__colorPlumas
    def setColorPlumas(self, color):
        self.__colorPlumas = color
    def movimiento(self):
        return 'volar'
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        new= Ave(nombre, edad, 'montañas', genero, "café glorioso")
        Ave.putListado(new)
        return new
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        new = Ave(nombre, edad, 'montañas', genero, "blanco y amarillo")
        Ave.putListado(new)
        return new
    @classmethod
    def putListado(cls, obj):
        if cls.__listado == None:
            cls.__listado = []
        cls.__listado.append(obj)
    @classmethod
    def cantidadAves(cls):
        if cls.__listado == None:
            return 0
        else:
            return len(cls.__listado)