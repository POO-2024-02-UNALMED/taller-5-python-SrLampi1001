""" from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
 """
class Animal:
    __TotalAnimales = 0
    def __init__(self, nombre = '', edad = 0, habitat = None, genero = 'ND', zona=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        self.__zona = zona
        Animal.__TotalAnimales += 1
    def movimiento(self):
        return 'desplazarse'
    def totalPorTipo(self):
        return "Mamiferos: " + str(Mamifero.cantidadMamiferos()) + "\n"+"Aves: " + str(Ave.cantidadAves()) + "\n"+"Reptiles: " + str(Reptil.cantidadReptiles()) + "\n" + "Peces: " + str(Pez.cantidadPeces()) + "\n"+"Anfibios: " + str(Anfibio.cantidadAnfibios());
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getEdad(self):
        return self.__edad;
    def setEdad(self, edad):
        self.__edad = edad
    def getHabitat(self):
        return self.__habitat
    def setHabitat(self, habitat):
        self.__habitat = habitat
    def getGenero(self):
        return self.__genero
    def setGenero(self, genero):
        self.__genero = genero
    def getZona(self):
        return self.__zona
    def setZona(self, zona):
        self.__zona=zona
    def __str__(self):
        if self.__zona==None:
            return 'Mi nombre es '+self.__nombre +', tengo una edad de '+ str(self.__edad) + ', habito en ' + str(self.__habitat) + ' y mi genero es ' + self.__genero
        else:
            return 'Mi nombre es '+self.__nombre +', tengo una edad de '+ str(self.__edad) + ', habito en ' + str(self.__habitat) + ' y mi genero es ' + self.__genero + ', la zona en la que me ubico es ' + str(self.__zona) + ', en el '+ str(self.__zona.getZoo())
    @classmethod
    def totalAnimales(cls):
        return cls.__TotalAnimales