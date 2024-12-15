from zooAnimales.animal import Animal
class Mamifero(Animal):
    __listado = None
    caballos = 0
    leones = 0
    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero, None)
        self.__pelaje = pelaje
        self.__patas = patas
    def isPelaje(self):
        return self.__pelaje
    def setPelaje(self, pelaje):
        self.__pelaje = pelaje
    def getPatas(self):
        return self.__patas
    def setPatas(self, patas):
        self.__patas = patas
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        new= Mamifero(nombre, edad, 'padera', genero, True, 4)
        Mamifero.putListado(new)
        return new
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        new = Mamifero(nombre, edad, 'selva', genero, True, 4)
        Mamifero.putListado(new)
        return new
    @classmethod
    def putListado(cls, obj):
        if cls.__listado == None:
            cls.__listado = []
        cls.__listado.append(obj)
    @classmethod
    def cantidadMamiferos(cls):
        if cls.__listado == None:
            return 0
        else:
            return len(cls.__listado)