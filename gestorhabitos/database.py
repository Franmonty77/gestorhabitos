import sqlite3

#Conexión a la base de datos
conexion = sqlite3.connect("habitos.db")
cursor=conexion.cursor()

#Crear tabla habitos
cursor.execute("""
CREATE TABLE IF NOT EXISTS habitos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)""")

# Crear tabla registro de habitos
cursor.execute("""
CREATE TABLE IF NOT EXISTS registro_habitos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_habito INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (id_habito) REFERENCES habitos(id)
)""")

#Guardar cambios
conexion.commit()

#Cerrar conexión
conexion.close()

print("Base de datos creada correctamente")