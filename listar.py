import sqlite3

conexion = sqlite3.connect("CAMAN_ALAGON_NAVARRO_almacen.db")
cursor = conexion.cursor()

consulta = """ SELECT * 
                FROM producto
                ORDER BY nombre
            """
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()

for producto in libros:
    print(producto)
conexion.close()