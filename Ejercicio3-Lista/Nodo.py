class Nodo:
    __prov=""
    __superficie=float
    __sig=None
    def insertar(self,provincia,superficie):
        self.__prov=provincia
        self.__superficie=superficie
    def insertarsig(self,nodo):
        self.__sig=nodo
    def obtenerprovsup(self):
        return self.__prov , self.__superficie
    def obtenersig(self):
        return self.__sig