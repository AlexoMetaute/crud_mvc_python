from model.database import Database

class UsuarioDAO:
    @staticmethod
    def crear_tabla():
        query = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        )
        """
        db = Database()
        db.ejecutar_consulta(query)
        db.cerrar_conexion()

    @staticmethod
    def agregar_usuario(nombre, email):
        query_check = "SELECT COUNT(*) FROM usuario WHERE email = %s"
        db = Database()
        resultado = db.obtener_datos(query_check, (email,))
        if resultado[0][0] > 0:
            print(f"⚠️ Error: El email '{email}' ya está registrado.")
        else:
            query_insert = "INSERT INTO usuario (nombre, email) VALUES (%s, %s)"
            db.ejecutar_consulta(query_insert, (nombre, email))
            print("✅ Usuario agregado correctamente.")
        db.cerrar_conexion()

    @staticmethod
    def obtener_usuarios():
        query = "SELECT * FROM usuario"
        db = Database()
        usuarios = db.obtener_datos(query)
        db.cerrar_conexion()
        return usuarios
