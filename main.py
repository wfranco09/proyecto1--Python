from json_db import DB

db = DB() # Inicialización de la base de datos

# Plantilla simplificada de tarea
task = {
    "status": 1,
    "name": "Example",
    "progress": 0,
    "created_by": "Luis"
}

# Añadir tarea a la base de datos
db.insert(task)
print(db)


# Obtener una tarea desde la base de datos
task_element = db.get(0)
print(task_element['uid']) # Mostrar el identificador único de la tarea


# Actualizar una tarea en la base de datos
task_edit = {
    "status": 0,
    "name": "Example",
    "progress": 0,
    "created_by": "Arturo"
}
db.update(0, task_edit) # Actualiza la tarea con índice 0
print(db)


# Eliminar una tarea en la base de datos
db.delete(0) # Elimina la tarea con índice 0
print(db)


# Limpiar base de datos (borrar todo)
db.clear()
print(db)
