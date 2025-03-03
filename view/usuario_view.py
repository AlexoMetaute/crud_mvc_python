from controller.usuario_controller import UsuarioController


class UsuarioView:
    @staticmethod
    def mostrar_menu():
        """Muestra el menú principal y maneja las opciones del usuario."""
        while True:
            print("\n--- MENÚ ---")
            print("1. Agregar usuario")
            print("2. Listar usuarios")
            print("3. Eliminar usuario")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del usuario: ")
                email = input("Ingrese el email del usuario: ")
                print(UsuarioController.crear_usuario(nombre, email))

            elif opcion == "2":
                usuarios = UsuarioController.listar_usuarios()
                print("\n--- Lista de Usuarios ---")
                for u in usuarios:
                    print(f"ID: {u[0]}, Nombre: {u[1]}, Email: {u[2]}")

            elif opcion == "3":
                id_usuario = input("Ingrese el ID del usuario a eliminar: ")
                if id_usuario.isdigit():
                    print(UsuarioController.eliminar_usuario(int(id_usuario)))
                else:
                    print("❌ Error: ID inválido.")

            elif opcion == "4":
                print("Saliendo del programa...")
                break

            else:
                print("❌ Opción no válida. Intente nuevamente.")
