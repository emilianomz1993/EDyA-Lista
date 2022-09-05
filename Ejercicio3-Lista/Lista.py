from Nodo import Nodo
class Lista:
    __cab=None
    __cant=int
    def __init__(self):
        self.__cant=0
    def insertar(self,provincia,superficie):
        if self.vacia():
            nodo=Nodo()
            nodo.insertar(provincia,superficie)
            self.__cab=nodo
            self.__cant+=1
        else:
            p,s=self.__cab.obtenerprovsup()
            if s>superficie:
                aux=self.__cab
                self.__cab=Nodo()
                self.__cab.insertar(provincia,superficie)
                self.__cab.insertarsig(aux)
            else:
                aux=self.__cab.obtenersig()
                if aux==None:
                    aux=Nodo()
                    aux.insertar(provincia,superficie)
                    self.__cab.insertarsig=aux
                else:
                    while bandera:
                        p,s=aux.obtenerprovsup()
                        if s>superficie:
                            nodo=Nodo()
                            nodo.insertarsig
    
    def vacia(self):
        return self.__cab==None



