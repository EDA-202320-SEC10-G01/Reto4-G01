"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import numpy as np
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {"malla_vial": None,
                    "vertices" : None,
                    "comparendos" : None}
    
    data_structs["malla_vial"] = gr.newGraph()
    
    
    return data_structs


# Funciones para agregar informacion al modelo

def añadir_arco_distancia(control, origen, destino, distancia):

    gr.addEdge(control["malla_vial"], origen, destino, distancia)
    
def añadir_vertice(control, vertice):
    
    gr.insertVertex(control["malla_vial"], vertice)


# Funciones de consulta

def req_1(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino):
    
    """
    Función que soluciona el requerimiento 1
    """
    
    origen, destino = obtener_vertices_cercanos(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino)
    
    grafo_a_recorrer = bfs.BreathFirstSearch(control["malla_vial"], origen)
    
    hay_camino = bfs.hasPathTo(grafo_a_recorrer, destino)
    
    if hay_camino:
        
        informacion = bfs.pathTo(grafo_a_recorrer, destino)
        
        vertices = lt.newList()
        
        while not st.isEmpty(informacion):
            
            lt.addLast(vertices, st.pop(informacion))
          
    else:
        
        vertices = None
    
    return vertices
            
        

def req_2(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino):
    
    """
    Función que soluciona el requerimiento 1
    """
    
    origen, destino = obtener_vertices_cercanos(control, latitud_inicial, longitud_inicial, latitud_final, longitud_final)
    
    grafo_a_recorrer = bfs.BreathFirstSearch(control["malla_vial"], origen)
    
    informacion = bfs.pathTo(grafo_a_recorrer, destino)
    
    return informacion
    

def req_3(control, localidad, n_camaras):
    """
    Función que soluciona el requerimiento 3
    """
    
    comparendos = control["comparendos"]
    
    lista_comparendos_localidad = []
    indices_comparendos_localidad = {}
    
    for comparendo in comparendos:
            
        if comparendo["18"] not in indices_comparendos_localidad:
                
            lista_comparendos_localidad.append({"vertice": comparendo["18"], "comparendos": 1})
            indices_comparendos_localidad[comparendo["18"]] = len(lista_comparendos_localidad) - 1
            
        else:
                
            lista_comparendos_localidad[indices_comparendos_localidad[comparendo["18"]]]["comparendos"] += 1
            
            
    lista_comparendos_localidad.sort(key = lambda x: x["comparendos"], reverse = True)
    
    vertices_subgrafo = lista_comparendos_localidad[:n_camaras]
    
    grafo_subgrafo = gr.newGraph()
    
    for vertice in vertices_subgrafo:
        
        gr.insertVertex(grafo_subgrafo, vertice["vertice"])
        
    for i in range(len(vertices_subgrafo)):
        
        for j in range(i + 1, len(vertices_subgrafo)):
            
            distancia = haversine_function(vertices_subgrafo[i]["vertice"][2], vertices_subgrafo[i]["vertice"][1], vertices_subgrafo[j]["vertice"][2], vertices_subgrafo[j]["vertice"][1])
            
            gr.addEdge(grafo_subgrafo, vertices_subgrafo[i]["vertice"], vertices_subgrafo[j]["vertice"], distancia)
            
    prim_mst = prim.PrimMST(grafo_subgrafo)
    
    return prim_mst
    


def haversine_function(lat1, lon1, lat2, lon2):
        
    earth_radius = 6371
        
    lat1 = np.radians(float(lat1))
    lat2 = np.radians(float(lat2))
    lon1 = np.radians(float(lon1))
    lon2 = np.radians(float(lon2))
        
    lat_diff = lat2 - lat1
    lon_diff = lon2 - lon1
        
    a = (np.sin(lat_diff/2))**2
    b = np.cos(lat1)
    c = np.cos(lat2)
    d = (np.sin(lon_diff/2))**2       
    e = a + b*c*d
        
        
    return 2 * earth_radius * np.arcsin(np.sqrt(e))


def obtener_vertices_cercanos(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino):
    
    vertice_origen = {"vertice": 0, "distancia": haversine_function(latitud_origen, longitud_origen, control["vertices"][0][2], control["vertices"][0][1])}
    vertice_destino = {"vertice": 0, "distancia": haversine_function(latitud_destino, longitud_destino, control["vertices"][0][2], control["vertices"][0][1])}
    
    for vertice in control["vertices"]:
        
        distancia = haversine_function(latitud_origen, longitud_origen, vertice[2], vertice[1])
        
        if distancia < vertice_origen["distancia"]:
            
            vertice_origen["vertice"] = vertice[0]
            vertice_origen["distancia"] = distancia
            
        if distancia < vertice_destino["distancia"]:
            
            vertice_destino["vertice"] = vertice[0]
            vertice_destino["distancia"] = distancia
            
    return vertice_origen["vertice"], vertice_destino["vertice"]
    
