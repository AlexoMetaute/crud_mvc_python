# CRUD con Flask, MySQL y MVC

Este proyecto es una aplicación web CRUD implementada siguiendo el patrón **MVC** (Modelo-Vista-Controlador) usando **Python**, **Flask** como framework web, **HTML** y **CSS** para la interfaz, y **MySQL** para el almacenamiento de datos.

La aplicación permite realizar las siguientes operaciones:
- **Crear:** Agregar nuevos usuarios.
- **Leer:** Listar todos los usuarios y buscar usuarios por nombre o email.
- **Actualizar:** Editar datos de un usuario.
- **Eliminar:** Borrar un usuario.

Además, se ha implementado un buscador en la vista para filtrar usuarios según su nombre o correo electrónico.

---

## Requisitos

- **Python 3.x** (se recomienda la última versión estable).
- **Flask**: Framework web para Python.
- **MySQL**: Motor de base de datos (puedes usar XAMPP, WAMP, MAMP, etc.).
- **mysql-connector-python**: Para conectar Python con MySQL.
- **pip**: Gestor de paquetes para Python.

---

## Instalación y Configuración

### 1. Clonar el repositorio o descargar el código fuente

Puedes clonar el repositorio mediante Git:
```bash
git clone <URL_DEL_REPOSITORIO>
````

## Crear el entorno virtual usando venv
python -m venv venv

# Activar el entorno virtual:
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

3. Instalar las dependencias
Con el entorno virtual activo (o globalmente), instala Flask y el conector de MySQL:

pip install flask mysql-connector-python

4. Configurar la Base de Datos
Abre phpMyAdmin, MySQL Workbench o tu herramienta de administración MySQL.
Crea una base de datos llamada crud_mvc_python

CREATE DATABASE crud_mvc_python;

Crea la tabla usuario ejecutando la siguiente consulta:
sql

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

(Opcional) Pobla la tabla con algunos datos de prueba:
sql

INSERT INTO usuario (nombre, email) VALUES
('Juan Pérez', 'juan@example.com'),
('Ana López', 'ana.lopez@example.com'),
('Carlos García', 'carlos@example.com'),
('María Rodríguez', 'maria@example.com'),
('Luis Hernández', 'luis@example.com'),
('Laura Sánchez', 'laura@example.com'),
('Miguel Torres', 'miguel.torres@example.com'),
('Sofía Martínez', 'sofia.martinez@example.com'),
('Diego Ramírez', 'diego.ramirez@example.com'),
('Elena Morales', 'elena.morales@example.com'),
('Javier Romero', 'javier.romero@example.com'),
('Valeria Vargas', 'valeria.vargas@example.com'),
('Ricardo Castro', 'ricardo.castro@example.com'),
('Gabriela Ortiz', 'gabriela.ortiz@example.com'),
('Esteban Rojas', 'esteban.rojas@example.com');

5. Verificar la Configuración de la Conexión
En el archivo model/database.py, asegúrate de que los parámetros de conexión sean correctos:

python

self.conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud_mvc_python"
)
Ajusta el usuario y la contraseña según tu entorno de MySQL.

Estructura del Proyecto
La estructura del proyecto es la siguiente:

php

crud_mvc_python/
├── app.py                # Archivo principal que inicia la aplicación Flask (controlador)
├── model/
│   ├── database.py       # Gestión de la conexión a MySQL
│   └── usuario.py        # (Opcional) Capa DAO para operaciones sobre la tabla 'usuario'
├── templates/            # Plantillas HTML (vistas)
│   ├── index.html        # Página principal (lista y buscador)
│   ├── agregar.html      # Formulario para agregar usuarios
│   ├── editar.html       # Formulario para editar usuarios
│   └── error.html        # Página para mostrar errores
├── static/               # Archivos estáticos (CSS, imágenes, etc.)
│   └── style.css         # Estilos CSS
└── README.md             # Documentación del proyecto (este archivo)

Ejecución de la Aplicación
Asegúrate de que el servidor MySQL esté en ejecución.
Desde la carpeta del proyecto, ejecuta:
bash

python app.py
Abre tu navegador y visita:

http://127.0.0.1:5000/
Verás la página principal del CRUD, donde podrás:
Agregar nuevos usuarios.
Ver el listado de usuarios.
Editar o eliminar usuarios.
Buscar usuarios por nombre o correo electrónico.
Funcionalidades Adicionales
Buscador
La página principal incluye un formulario de búsqueda que te permite filtrar usuarios por nombre o email.
Al ingresar un término de búsqueda y enviar el formulario, se mostrarán únicamente los usuarios que coincidan.
Si se realiza una búsqueda, se mostrará un botón "Volver al inicio" para regresar al listado completo.
Tecnologías Utilizadas
Python: Lenguaje de programación principal.
Flask: Framework web utilizado para implementar el patrón MVC, gestionar rutas y renderizar plantillas con Jinja.
MySQL: Motor de base de datos para almacenar la información.
HTML/CSS: Para la estructura y el diseño de la interfaz web.
mysql-connector-python: Módulo para conectar Python con MySQL.

