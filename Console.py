import tabulate
import csv

from Nodo import Nodo
from Arco import Arco
from Grafo import Grafo
from Dijkstra import algoritmo_Dijkstra
from BellmanFord import algoritmo_Bellman_Ford


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


def introducir_grafo_archivos()->Grafo:
    print("Introduzca el nombre del archivo CSV de los nodos del grafo: ")
    nombre_archivo = input()
    nombre_archivo = "archivos_grafos/entradas/"+nombre_archivo
    
    nodos_Grafo = []
    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)
        for n in lector_csv:
            nodo = Nodo(n[0])
            nodos_Grafo.append(nodo)
            print(n)
    
    grafo = Grafo(nodos_Grafo)
    print('\n Nodos introducidos \n')
    
    print('Introducir el nombre del archivo CSV con lo arcos del grafo: ')
    nombre_archivo = input()
    nombre_archivo = "archivos_grafos/entradas/"+nombre_archivo

    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)
        for arco in lector_csv:
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

def generar_archivo_Dijkstra(tabla:list, titulos:list, contador:int):
    nombre_archivo = "tabla_resultante_" + str(contador)+".csv"
    ruta_archivo = "archivos_grafos/respuestas/"+nombre_archivo

    headers = []

    headers.append(titulos[1])

    titulos = titulos[2:]

    contenido_archivo = []

    for titulo in titulos:
        headers.append(titulo)
        headers.append("p"+titulo)
    
    contenido_archivo.append(headers)

    for fila in tabla:
        fila_contenido = [fila[1]]
        for f in fila[2:]:
            fila_contenido.append(f[1])
            fila_contenido.append(f[0])
        contenido_archivo.append(fila_contenido.copy())

    with open(ruta_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        for fila in contenido_archivo:
            escritor_csv.writerow(fila)
    
    print("\nPuede consultar la tabla en formato CSV en la ruta\n", ruta_archivo)

def generar_archivo_BellmanFord(iteraciones:dict, nodos:list):

    for n in nodos:
        nombre_archivo = n + ".csv"
        ruta_archivo = "archivos_grafos/respuestas/"+nombre_archivo
        contenido_archivo = []
        contenido_archivo.append(nodos.copy())

        for fila in iteraciones[n]:
            nueva_entrada = []
            for entrada in fila:
                nueva_entrada.append(entrada[0])
                nueva_entrada.append(entrada[1])
            contenido_archivo.append(nueva_entrada.copy())
        
        with open(ruta_archivo, mode='w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for fila in contenido_archivo:
                escritor_csv.writerow(fila)


def iniciar_aplicacion():
    print('-------------------Estado Enlace Algoritmo----------------------')
    print()

    print("Seleciona la opción por la cual quieres ingresar los grafos: ")
    print("1- Mediante Archivos")
    print("2- Manualmente")
    inicio = input()
    
    if inicio == "1":
        grafo = introducir_grafo_archivos()
    elif inicio == "2":
        grafo = introducir_grafo_listas()
    else:
        print("Opcion no valida: ")
        return None
    
    option = ""
    aux = 0
    while True:
        print("\nQue algoritmo desea ejecutar: ")
        print("1- Algoritmo Estado Enlace")
        print("2- Aljoritmo Vector Distancia")

        option = input()
        if option == "1":
            nodoI = input("\nEscribe en nombre del nodo inicial: ")
            nodoInicial = grafo.obtener_nodo(nodoI)

            while nodoInicial == None:
                print("El nodo no existe")
                nodoI = input("Escribe el nombre del nodo inicial: ")
                nodoInicial = grafo.obtener_nodo(nodoI)

            respuesta = algoritmo_Dijkstra(grafo, nodoInicial)
            tabla = respuesta[0]
            titulos = respuesta[1]

            generar_archivo_Dijkstra(tabla, titulos, aux)
            print()
            aux += 1
        elif option == "2":
            resultado = algoritmo_Bellman_Ford(grafo)
            iteraciones = resultado[0]
            nodos = resultado[1]
            generar_archivo_BellmanFord(iteraciones, nodos)
            print("\nConsulta los archivos generados en archivos_grafo/respuestas/\n")
        else:
            print("Fin del programa")
            break

    

iniciar_aplicacion()