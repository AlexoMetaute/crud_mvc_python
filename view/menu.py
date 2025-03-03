from model.usuario import UsuarioDAO

def mostrar_menu():
    while True:
        print("\n===== MENÚ DE USUARIOS =====")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            UsuarioDAO.agregar_usuario(nombre, email)

        elif opcion == "2":
            usuarios = UsuarioDAO.obtener_usuarios()
            if usuarios:
                print("\n🔹 Usuarios Registrados:")
                for u in usuarios:
                    print(f"ID: {u[0]} | Nombre: {u[1]} | Email: {u[2]}")
            else:
                print("⚠️ No hay usuarios registrados.")

        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.")

