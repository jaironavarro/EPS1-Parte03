# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:08:20 2022

@author: user
"""


import sqlite3

conexion = sqlite3.connect("CAMAN_ALAGON_NAVARRO_almacen.db")

tabla_producto = """CREATE TABLE producto(idproducto INTEGER PRIMARY KEY AUTOINCREMENT,codigo TEXT UNIQUE,nombre TEXT,precio REAL)"""

cursor = conexion.cursor()
cursor.execute(tabla_producto)


print ("Menu de Opciones \n1. Registrar \n2. Eliminar \n3. Editar \n4. Listar \n5. Salir")

opcion=int(input("Digite la opcion que desea realizar: "))


conexion.close()
