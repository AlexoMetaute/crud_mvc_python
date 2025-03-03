import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crud_mvc_python"
    )
    cursor = conn.cursor()

    # Consulta los datos de la tabla `usuarios`
    cursor.execute("SELECT * FROM usuarios;")
    users = cursor.fetchall()

    if users:
        print("Usuarios encontrados en la base de datos:")
        for user in users:
            print(user)
    else:
        print("No hay usuarios en la base de datos.")

    cursor.close()
    conn.close()
except mysql.connector.Error as e:
    print("Error de conexión:", e)
