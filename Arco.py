from Nodo import Nodo

class Arco:
    def __init__(self, nodoO:Nodo, nodoD:Nodo, peso:int):
        self.nodoO = nodoO
        self.nodoD = nodoD
        self.peso = peso
    
    def obtener_nodoO(self):
        return self.nodoO
    
    def obtener_nodoD(self):
        return self.nodoD

    def obtener_peso(self):
        return self.peso