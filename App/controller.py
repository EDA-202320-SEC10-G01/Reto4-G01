﻿"""
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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    return model.new_data_structs()


# Funciones para la carga de datos

def load_data(control):
    
    tracemalloc.start()
    tiempo_carga = get_time()
    memoria_carga = get_memory()
    
    vertices = cf.data_dir + f"tickets/bogota_vertices.txt"
    arcos = cf.data_dir + f"tickets/bogota_arcos.txt"
    comparendos = cf.data_dir + f"tickets/comparendos_2019_bogota_vertices.csv"
    
    archivo_vertices = list(csv.reader(open(vertices, encoding="utf-8"), delimiter=","))
    archivo_arcos = list(csv.reader(open(arcos, encoding="utf-8"), delimiter=" "))
    archivo_comparendos = list(csv.reader(open(comparendos, encoding="utf-8"), delimiter=","))
    
    
    
    for linea in archivo_vertices:

        identificador, longitud, latitud = linea
        model.añadir_vertice(control, int(identificador))
        

    for linea in archivo_arcos:

        if len(linea) == 1:
            pass
        else:
            
            vertice_principal = linea[0]
            info_principal = archivo_vertices[int(vertice_principal)]
            
            vertices_a_conectar = linea[1:]
            
            for vertice in vertices_a_conectar:
                
                info_a_conectar = archivo_vertices[int(vertice)]
                
                lat1 = info_a_conectar[2]
                lon1 = info_a_conectar[1]
                lat2 = info_principal[2]
                lon2 = info_principal[1]
                
                distancia = model.haversine_function(lat1, lon1, lat2, lon2)
                
                model.añadir_arco_distancia(control, int(vertice), int(vertice_principal), distancia)
                
    control["vertices"] = archivo_vertices
    control["comparendos"] = archivo_comparendos
   

    tiempo_carga = delta_time(tiempo_carga, get_time())
    memoria_carga = delta_memory(get_memory(), memoria_carga)
    numero_vertices = model.gr.numVertices(control["malla_vial"])
    numero_arcos = model.gr.numEdges(control["malla_vial"])
    
    tracemalloc.stop()
    
    return tiempo_carga, memoria_carga, numero_vertices, numero_arcos


def req_1(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino):
    """
    Retorna el resultado del requerimiento 1
    """
    
    tracemalloc.start()
    tiempo_req_1 = get_time()
    memoria_req_1 = get_memory()
    
    model_response = model.req_1(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino)
    
    tiempo_req_1 = delta_time(tiempo_req_1, get_time())
    memoria_req_1 = delta_memory(get_memory(), memoria_req_1)
    
    tracemalloc.stop()
    
    return tiempo_req_1, memoria_req_1, model_response
    


def req_2(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino):
    """
    Retorna el resultado del requerimiento 2
    """
    tracemalloc.start()
    tiempo_req_1 = get_time()
    memoria_req_1 = get_memory()
    
    model_response = model.req_1(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino)
    
    tiempo_req_1 = delta_time(tiempo_req_1, get_time())
    memoria_req_1 = delta_memory(get_memory(), memoria_req_1)
    
    tracemalloc.stop()
    
    return tiempo_req_1, memoria_req_1, model_response


def req_3(control, localidad, n_camaras):
    """
    Retorna el resultado del requerimiento 3
    """
    tracemalloc.start()
    tiempo_req_1 = get_time()
    memoria_req_1 = get_memory()
    
    model_response = model.req_1(control, localidad, n_camaras)
    
    tiempo_req_1 = delta_time(tiempo_req_1, get_time())
    memoria_req_1 = delta_memory(get_memory(), memoria_req_1)
    
    tracemalloc.stop()
    
    return tiempo_req_1, memoria_req_1, model_response


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control,origen_lat,origen_lon,destino_lat,destino_lon):
    return model.req_7(control["model"],origen_lat,origen_lon,destino_lat,destino_lon)

    

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter())


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024000.0
    return delta_memory
