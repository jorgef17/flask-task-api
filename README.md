# Tareas API con Flask

## Descripción
Esta es una API  simple construida con Flask para gestionar tareas. Permite las operaciones básicas de crear, leer, actualizar y eliminar tareas (CRUD). La API utiliza autenticación básica para la seguridad, y los datos de las tareas se almacenan en un archivo JSON.

Es ideal como ejemplo básico para aprender sobre el desarrollo de APIs con Python y Flask.

## Funcionalidades
- **GET /tasks**: Obtener todas las tareas.
- **POST /tasks**: Crear una nueva tarea.
- **PUT /tasks/<id>**: Actualizar una tarea existente.
- **DELETE /tasks/<id>**: Eliminar una tarea.

## Requisitos
- Python 3.x
- Flask
- Flask-HTTPAuth

## Instalación
1. Clona el repositorio:
    ```bash
    git clone https://github.com/jorgef17/flask-task-api.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd flask-task-api
    ```
3. Instala los requisitos:
    ```bash
    pip install -r requirements.txt
    ```

4. Ejecuta el servidor:
    ```bash
    python app.py
    ```

El servidor estará corriendo en `http://127.0.0.1:5000/` por defecto.

## Uso
- Para interactuar con la API, se requiere autenticación básica. El usuario es `admin` y la contraseña es `1234`.
- Usa herramientas como Postman o Curl para probar los endpoints de la API.

## Contribución
Si deseas contribuir, por favor realiza un fork del repositorio y envía un pull request con las mejoras o correcciones que hayas realizado.

