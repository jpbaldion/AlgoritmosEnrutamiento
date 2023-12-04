# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:55:44 2023

@author: baldi
"""
from tabulate import tabulate
import math

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


def algoritmo_Dijkstra(grafo:Grafo, nodoInicial:Nodo):
    tabla = []
    nodosTabla = []
    headersTabla = ["Paso", "Nodo"]
    nodosIndices = { "Paso": 0, "Nodo": 1, }
    
    nodos_grafo = grafo.obtener_nodos()
    
    indice = 2
    for n in nodos_grafo:
        nombreGrafo = n.obtener_nombre()
        nodosTabla.append(nombreGrafo)
        nodosIndices[nombreGrafo] = indice
        indice += 1


    vecinos = nodoInicial.obtener_vecinos()

    indice = 1

    fila = list(range(0, len(nodos_grafo)+2))
    fila[0] = indice 
    fila[1] = nodoInicial.obtener_nombre()
    
    nodosVisitados = [nodoInicial.obtener_nombre()]
    fila[nodosIndices[nodoInicial.obtener_nombre()]] = [nodoInicial.obtener_nombre(), 0]
    
    # Inicialización

    for n in nodosTabla:
        if n not in nodosVisitados:
            if n in vecinos:
                arco = grafo.obtener_arco(nodoInicial.obtener_nombre(), n)
                fila[nodosIndices[n]] = [nodoInicial.obtener_nombre(), arco.obtener_peso()]
            else:
                fila[nodosIndices[n]] = ["", math.inf]

    tabla.append(fila.copy())

    # Recorrido de los nodos
    while len(nodosTabla) != len(nodosVisitados):
        ultima_iteracion = tabla[-1][2:]
        min = math.inf
        
        i = 0
        indice_menor = None
        for entrada in ultima_iteracion:
            if grafo.obtener_nodo(nodosTabla[i]).obtener_nombre() not in nodosVisitados:
                if entrada[1] <= min:
                    min = entrada[1]
                    indice_menor = i
            i += 1
        
        nodo_nombre_evaluar = nodosTabla[indice_menor]
        nodo_evaluar = grafo.obtener_nodo(nodo_nombre_evaluar)
        indice += 1
        vecinos = nodo_evaluar.obtener_vecinos()
        nodosVisitados.append(nodo_evaluar.obtener_nombre())
        fila[0] = indice
        fila[1] = nodo_evaluar.obtener_nombre()

        for v in vecinos:
            peso_actual = ultima_iteracion[indice_menor][1]
            arc = grafo.obtener_arco(nodo_evaluar.obtener_nombre(), v)
            peso = arc.obtener_peso()
            entrada = ultima_iteracion[nodosIndices[v]-2]
            peso_entrada = entrada[1]
            
            if peso + peso_actual < peso_entrada:
                fila[nodosIndices[v]] = [nodo_evaluar.obtener_nombre(), peso + peso_actual]

        tabla.append(fila.copy())

    headersTabla = headersTabla + nodosTabla
    print("\n\n---- Tabla Resultante ----")
    print(tabulate(tabla, headers=headersTabla))


def introducir_grafo_manual()->Grafo:
    print("Introduce todos los grafos que pertenecen a tu grafo: ")
    print("Cuando termines escribe FIN")
    option = ""
    nodos = []
    while option != "FIN":
        option = input("Introduce el nombre del nodo:")
        if option != "FIN":
            if option in nodos:
                print("Ya existe un nodo con ese nombre")
            else:
                nodos.append(option)
                print("Nodo Agregado: " + option)
    
    nodosGrafo = []
    for n in nodos:
        nodo = Nodo(n)
        nodosGrafo.append(nodo)
    
    grafo = Grafo(nodosGrafo)

    arco = ""
    print("Ahora agrega los arcos del nodo")
    print("Ingrese el arco en le seguiente formato: x-p-y")
    print("  x - Es el nombre del nodo de origen")
    print("  p - Es el peso del arco")
    print("  y - Es el nombre del nodo de destino")
    print("Ingrese FIN para acabar de ingresar los arcos")
    while arco != "FIN":
        arco = input("Arco: ")
        if arco != "FIN":
            elementos_arco = arco.split("-")
            if len(elementos_arco) == 3:
                nodoO = elementos_arco[0]
                peso = elementos_arco[1]
                nodoD = elementos_arco[2]

                if peso.isdigit():
                    peso = int(peso)
                else:
                    print("el peso debe ser un entero")
                    continue
                
                grafo.agregar_arco(nodoO, peso, nodoD)

    print("Arcos Agregados: ")
    arcos = grafo.obtener_arcos()
    print(grafo.obtener_arco("a", "b"))
    for a in arcos:
        print(a.obtener_nodoO().obtener_nombre(), "-", a.obtener_peso(), "-", a.obtener_nodoD().obtener_nombre())

    return grafo


def introducir_grafo_listas()->Grafo:
    nodos = []
    print("Para introducir el grafo primero define los nodos y luego los arcos")
    print("Para definir los nodos introduce todos los nombres de los nodos separados por punto y coma.")
    print("Ejemplo: n1,n2,n3,n4,n5,n6")
    nombres_nodo = input()
    nombres_nodo = nombres_nodo.replace(" ", "")
    nodos = nombres_nodo.split(",")
    nodos = list(set(nodos))
    nodosGrafo=[]
    for n in nodos:
        nodo = Nodo(n)
        nodosGrafo.append(nodo)
    grafo = Grafo(nodosGrafo)
    print("Nodos Agregados", nodos)

    print("Ahora introduce los arcos como tuplas de 3 poscisiones (x,y,c) separadas por coma")
    print("donde x es el nodo origen, y el nodo de destino y c el costo del nodo (no puede ser negativo)")
    print("Ejemplo: (n1,n2,4),(n1,n3,3),(n2,n4,5),(n3,n6,8),(n1,n5,1)")
    arcos = []
    arcos_input = input()
    arcos_input = arcos_input.replace(" ", "")
    arcos_input = arcos_input.rstrip(")")
    arcos_input = arcos_input.lstrip("(")
    arcos_input = arcos_input.split("),(")
    for arc in arcos_input:
        a = arc.split(',')
        arcos.append(a)

    for arco in arcos:
        nodoO = arco[0]
        nodoD = arco[1]
        peso = arco[2]

        if peso.isdigit():
            peso = int(peso)
        else:
            print("el peso debe ser un entero")
            continue

        grafo.agregar_arco(nodoO, peso, nodoD)

    return grafo


def iniciar_aplicacion():
    print('-------------------Estado Enlace Algoritmo----------------------')
    print()

    print("Seleciona la opción por la cual quieres ingresar los grafos: ")
    print("1- Manualmente uno a uno")
    print("2- Manualmente en conjuntos")
    inicio = input()
    
    if inicio == "1":
        grafo = introducir_grafo_manual()
    elif inicio == "2":
        grafo = introducir_grafo_listas()
    else:
        print("Opcion no valida: ")
        return None
    
    option = ""
    while True:
        print("Que algoritmo desea ejecutar: ")
        print("1- Algoritmo Lista Enlace")
        print("2- Aljoritmo Vector Distancia")

        option = input()
        if option == "1":
            nodoI = input("Escribe en nombre del nodo inicial: ")
            nodoInicial = grafo.obtener_nodo(nodoI)

            while nodoInicial == None:
                print("El nodo no existe")
                nodoI = input("Escribe el nombre del nodo inicial: ")
                nodoInicial = grafo.obtener_nodo(nodoI)

            algoritmo_Dijkstra(grafo, nodoInicial)
        else:
            print("Fin del programa")
            break


iniciar_aplicacion()