from flask import Flask, jsonify, request
import json
from flask_httpauth import HTTPBasicAuth
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# Crear la instancia de API
api = Api(app, doc='/docs')

# Ruta del archivo JSON
TASKS_FILE = 'tasks.json'

# Cargar tareas desde el archivo
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):  # Asegura que sea una lista
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Guardar tareas en el archivo
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Verificación de la autenticación
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == '1234':
        return True
    return False

# Definir el modelo de tarea con Flask-RESTX
task_model = api.model('Task', {
    'id': fields.Integer(required=True, description='ID de la tarea'),
    'title': fields.String(required=True, description='Título de la tarea'),
    'completed': fields.Boolean(default=False, description='Estado de la tarea')
})

# Obtener todas las tareas
@api.route('/tasks')
class TaskList(Resource):
    @auth.login_required
    def get(self):
        """Obtener todas las tareas"""
        tasks = load_tasks()
        return tasks  

    @auth.login_required
    @api.expect(task_model)  # Esperar el modelo de tarea
    def post(self):
        """Crear una nueva tarea"""
        tasks = load_tasks()
        data = request.get_json()

        if 'title' not in data or not data['title']:
            return {'error': 'El título de la tarea es obligatorio'}, 400

        new_task = {
            'id': len(tasks) + 1,
            'title': data['title'],
            'completed': False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        return new_task, 201  

# Actualizar una tarea
@api.route('/tasks/<int:task_id>')
class Task(Resource):
    @auth.login_required
    def put(self, task_id):
        """Actualizar una tarea existente"""
        tasks = load_tasks()
        data = request.get_json()

        for task in tasks:
            if task['id'] == task_id:
                task['title'] = data.get('title', task['title'])
                task['completed'] = data.get('completed', task['completed'])
                save_tasks(tasks)
                return task  

        return {'error': 'Tarea no encontrada'}, 404

    @auth.login_required
    def delete(self, task_id):
        """Eliminar una tarea"""
        tasks = load_tasks()
        new_tasks = [task for task in tasks if task['id'] != task_id]

        if len(tasks) == len(new_tasks):
            return {'error': 'Tarea no encontrada'}, 404

        save_tasks(new_tasks)
        return {'message': 'Tarea eliminada exitosamente'}, 200

if __name__ == '__main__':
    app.run(debug=True)
