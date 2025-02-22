﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import threading

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    return controller.new_controller()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    print("\nCargando información de los archivos ....")
    tiempo, memoria, vertices, arcos = controller.load_data(control)
    print("\nInformación cargada exitosamente.")
    print(f"Tiempo de carga: {tiempo} segundos")
    print(f"Memoria usada: {memoria} megabytes")
    print(f"Numero de vertices: {vertices}")    
    print(f"Numero de arcos: {arcos}\n")
    
    

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    latitud_origen = input("Ingrese la latitud del origen: ")
    longitud_origen = input("Ingrese la longitud del origen: ")
    latitud_destino = input("Ingrese la latitud del destino: ")
    longitud_destino = input("Ingrese la longitud del destino: ")
    
    controller_response = controller.req_1(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino)
    
    print("-----------Requerimiento 1-----------")
    print("Tiempo de ejecución: ", controller_response[0])
    print("Memoria usada: ", controller_response[1])
    print("Camino: ", controller_response[2])

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    latitud_origen = input("Ingrese la latitud del origen: ")
    longitud_origen = input("Ingrese la longitud del origen: ")
    latitud_destino = input("Ingrese la latitud del destino: ")
    longitud_destino = input("Ingrese la longitud del destino: ")
    
    print(controller.req_1(control, latitud_origen, longitud_origen, latitud_destino, longitud_destino))

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control,latsup,latsdown,lonleft,lonright):
    lato = input("Ingrese la latitud del origen: ")
    lono = input("Ingrese la longitud del origen: ")
    latd = input("Ingrese la latitud del destino: ")
    lond = input("Ingrese la longitud del destino: ")
    if lond<latsdown or lond>latsup or lono<lonleft or lono>lonright:
        print("Coordenadas fuera del rango")
    elif latd<latsdown or latd>latsup or lato<lonleft or lato>lonright:
        print("Coordenadas fuera del rango")
    else: 
        path,distancia = controller.req_7(control,lato,lono,latd,lond)
        print("La distancia es de: ",km)
        print("El camino es: ",path) 
        print("Los vértices son:",lt.size(path))       


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
def thread_cycle():
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
            
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

if __name__ == "__main__":
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()
    """
    Menu principal
    """
