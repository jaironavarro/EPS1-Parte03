import sqlite3
conexion = sqlite3.connect("CAMAN_ALAGON_NAVARRO_almacen.db")
cursor = conexion.cursor()

A = input("Digite el codigo: ")
B = input("Digite el nombre: ")
C = input("Digite el precio: ")

registrar_producto= [(A,B,C)]


consulta_producto=""" INSERT INTO
                    producto(codigo, nombre, precio)
                    VALUES(?,?,?)
               """
cursor.executemany(consulta_producto,registrar_producto)
conexion.commit()
conexion.close()