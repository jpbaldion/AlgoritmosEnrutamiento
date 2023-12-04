class Nodo:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.vecinos = []
    
    def obtener_nombre(self):
        return self.nombre
    
    def agregar_vecino(self,nombreVecino: str):
        self.vecinos.append(nombreVecino)

    def obtener_vecinos(self):
        return self.vecinos

    def es_vecino(self, nodo):
        if nodo in self.vecinos:
            return True
        return False