import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crud_mvc_python"
            )
            self.cursor = self.conexion.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"❌ Error de conexión a la base de datos: {e}")

    def ejecutar_consulta(self, consulta, parametros=None):
        if parametros is None:
            parametros = ()
        try:
            self.cursor.execute(consulta, parametros)
            self.conexion.commit()
        except mysql.connector.Error as e:
            print(f"❌ Error en ejecutar_consulta(): {e}")

    def obtener_datos(self, consulta, parametros=None):
        if parametros is None:
            parametros = ()
        try:
            self.cursor.execute(consulta, parametros)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"❌ Error en obtener_datos(): {e}")
            return []

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
