from flask import Flask, render_template, request, redirect, url_for
from model.database import Database

app = Flask(__name__)
db = Database()

# Página principal: muestra todos los registros o, si se realiza una búsqueda, los resultados filtrados.
@app.route('/')
def index():
    try:
        usuarios = db.obtener_datos("SELECT * FROM usuario")
        return render_template('index.html', usuarios=usuarios)
    except Exception as e:
        print(f"❌ Error en index(): {e}")
        return render_template('error.html', mensaje=f"Error al cargar la página principal: {e}")

# Ruta para búsqueda de usuarios (por nombre o email)
@app.route('/buscar', methods=['GET'])
def buscar_usuario():
    try:
        termino = request.args.get('query', '').strip()
        if termino:
            consulta = "SELECT * FROM usuario WHERE nombre LIKE %s OR email LIKE %s"
            parametro = f"%{termino}%"
            usuarios = db.obtener_datos(consulta, (parametro, parametro))
        else:
            usuarios = db.obtener_datos("SELECT * FROM usuario")
        return render_template('index.html', usuarios=usuarios)
    except Exception as e:
        print(f"❌ Error en buscar_usuario(): {e}")
        return render_template('error.html', mensaje=f"Error en la búsqueda: {e}")

# Formulario para agregar usuario (GET)
@app.route('/agregar', methods=['GET'])
def mostrar_formulario_agregar():
    return render_template('agregar.html')

# Procesar formulario para agregar usuario (POST)
@app.route('/agregar', methods=['POST'])
def agregar_usuario():
    try:
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        if not nombre or not email:
            return render_template('error.html', mensaje="Nombre y email son obligatorios.")
        query = "INSERT INTO usuario (nombre, email) VALUES (%s, %s)"
        db.ejecutar_consulta(query, (nombre, email))
        return redirect(url_for('index'))
    except Exception as e:
        print(f"❌ Error en agregar_usuario(): {e}")
        return render_template('error.html', mensaje=f"Error al agregar usuario: {e}")

# Formulario para editar usuario (GET)
@app.route('/editar/<int:id>', methods=['GET'])
def mostrar_formulario_editar(id):
    try:
        usuario = db.obtener_datos("SELECT * FROM usuario WHERE id = %s", (id,))
        if not usuario:
            return render_template('error.html', mensaje="Usuario no encontrado.")
        return render_template('editar.html', usuario=usuario[0])
    except Exception as e:
        print(f"❌ Error en mostrar_formulario_editar(): {e}")
        return render_template('error.html', mensaje=f"Error al cargar formulario de edición: {e}")

# Procesar edición de usuario (POST)
@app.route('/editar/<int:id>', methods=['POST'])
def editar_usuario(id):
    try:
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        if not nombre or not email:
            return render_template('error.html', mensaje="Nombre y email son obligatorios.")
        query = "UPDATE usuario SET nombre = %s, email = %s WHERE id = %s"
        db.ejecutar_consulta(query, (nombre, email, id))
        return redirect(url_for('index'))
    except Exception as e:
        print(f"❌ Error en editar_usuario(): {e}")
        return render_template('error.html', mensaje=f"Error al actualizar usuario: {e}")

# Eliminar usuario (GET)
@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_usuario(id):
    try:
        query = "DELETE FROM usuario WHERE id = %s"
        db.ejecutar_consulta(query, (id,))
        return redirect(url_for('index'))
    except Exception as e:
        print(f"❌ Error en eliminar_usuario(): {e}")
        return render_template('error.html', mensaje=f"Error al eliminar usuario: {e}")

if __name__ == '__main__':
    app.run(debug=True)
