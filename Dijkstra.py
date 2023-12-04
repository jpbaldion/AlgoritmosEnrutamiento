from Nodo import Nodo
from Arco import Arco
from Grafo import Grafo
import math
from tabulate import tabulate

def algoritmo_Dijkstra(grafo:Grafo, nodoInicial:Nodo):
    tabla = []
    nodosTabla = []
    headersTabla = ["Step", "N'"]
    nodosIndices = {"Step": 0, "N'": 1,}
    
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
    Nprima = fila[1]
    
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
        Nprima += nodo_evaluar.obtener_nombre()
        fila[1] = Nprima

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
    return tabla, headersTabla