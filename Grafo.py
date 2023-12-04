from Nodo import Nodo
from Arco import Arco

class Grafo:
    
    def __init__(self, nodos:list):
        self.nodos = nodos
        self.arcos = []
        
    
    def obtener_nodos(self):
        return self.nodos

    def agregar_arco(self, nodoO:str, peso:int, nodoD:str):
        origen = self.obtener_nodo(nodoO)
        destino = self.obtener_nodo(nodoD)
        if origen != None and  destino != None:
            if peso >= 0:
                arco1 = Arco(origen, destino, peso)
                arco2 = Arco(destino, origen, peso)

                self.arcos.append(arco1)
                self.arcos.append(arco2)

                origen.agregar_vecino(nodoD)
                destino.agregar_vecino(nodoO)
            else:
                print("Los arcos deben tener pesos positivos")
        else:
            print("Los nodos no existen")

    def obtener_nodo(self, nombre_nodo:str)->Nodo:
        for nodo in self.nodos:
            if nodo.obtener_nombre() == nombre_nodo:
                return nodo
        return None

    def obtener_arcos(self):
        return self.arcos
    
    def obtener_arco(self, nodoO, nodoD)->Arco:
        origen = self.obtener_nodo(nodoO)
        destino = self.obtener_nodo(nodoD)
        for arco in self.arcos:
            if origen is arco.obtener_nodoO() and destino is arco.obtener_nodoD():
                return arco
        return None