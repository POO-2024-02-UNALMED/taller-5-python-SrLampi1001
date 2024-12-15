class Zoologico:
    def __init__(self, nombre = '', ubicacion= None, zonas= None):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__zonas = zonas
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getUbicacion(self):
        return self.__ubicacion
    def setUbicacion(self, ubicacion):
        self.__ubicacion=ubicacion
    def agregarZonas(self, zona):
        if self.__zonas == None:
            self.__zonas=[]
        self.__zonas.append(zona)
    def getZona(self):
        return self.__zonas
    def cantidadTotalAnimales(self):
        cnt = 0
        for el in self.__zonas:
            if not(el.getAnimales() == None):
                cnt += el.cantidadAnimales()
        return cnt
    def __str__(self):
        return self.__nombre;