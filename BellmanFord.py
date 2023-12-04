from Nodo import Nodo
from Arco import Arco
from Grafo import Grafo
import math
from tabulate import tabulate

def algoritmo_Bellman_Ford(grafo:Grafo):
    nodos_grafo = grafo.obtener_nodos()
    
    nodosIndices = {}
    nodos_nombres = []
    
    indice = 0
    for n in nodos_grafo:
        nombreGrafo = n.obtener_nombre()
        nodos_nombres.append(nombreGrafo)
        nodosIndices[nombreGrafo] = indice
        indice += 1

    tabla = {}
    for nodo in nodos_grafo:
        nodo_actual = nodo.obtener_nombre()
        vecinos_n = nodo.obtener_vecinos()
        tabla[nodo_actual] = []
        fila = []
        for n in nodos_nombres:
            if n in vecinos_n:
                arco_vecino = grafo.obtener_arco(nodo_actual, n)
                costo_vecino = arco_vecino.obtener_peso()
                entrada = [costo_vecino, n]
            elif n == nodo_actual:
                entrada = [0, n]
            else:
                entrada = [math.inf, n]
            fila.append(entrada)
        
        tabla[nodo_actual].append(fila)
    while True:
        parar = True
        for n, VD in tabla.items():
            for n1, VD1 in tabla.items():
                if n != n1:
                    vector_actual = VD[-1]
                    vector_comprobar = VD1[-1]
                    
                    costo_inicial = vector_actual[nodosIndices[n1]][0]

                    i = 0
                    nueva_entrada = []
                    while i < len(vector_actual):
                        valor_actual = vector_actual[i]
                        valor_comparar = vector_comprobar[i]
                        if n == valor_comparar[1]:
                            nueva_entrada.append(valor_actual.copy())
                        else:
                            if costo_inicial + valor_comparar[0] < valor_actual[0]:
                                nueva_entrada.append([costo_inicial + valor_comparar[0], n1])
                                parar = False
                            else:
                                nueva_entrada.append(valor_actual.copy())
                        i += 1
                    
                    tabla[n].append(nueva_entrada.copy())

        if parar:
            break

    for clave, valor in tabla.items():
        print(f"\nIteraciones del nodo {clave}")
        
        print(tabulate(valor, headers=nodos_nombres))
    
    return tabla, nodos_nombres