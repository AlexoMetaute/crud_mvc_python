from model.usuario import UsuarioDAO

class UsuarioController:
    @staticmethod
    def crear_usuario(nombre, email):
        """Crea un nuevo usuario en la base de datos."""
        try:
            UsuarioDAO.agregar_usuario(nombre, email)
            return f"Usuario '{nombre}' agregado correctamente."
        except Exception as e:
            return f"Error al agregar usuario: {str(e)}"

    @staticmethod
    def listar_usuarios():
        """Obtiene y retorna la lista de usuarios."""
        usuarios = UsuarioDAO.obtener_usuarios()
        return [(u.id, u.nombre, u.email) for u in usuarios]

    @staticmethod
    def eliminar_usuario(id_usuario):
        """Elimina un usuario por su ID."""
        try:
            UsuarioDAO.eliminar_usuario(id_usuario)
            return f"Usuario con ID {id_usuario} eliminado correctamente."
        except Exception as e:
            return f"Error al eliminar usuario: {str(e)}"
