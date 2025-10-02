from json_db import DB # traer la clase DB
from datetime import datetime # para manejar fechas y horas

class TaskManager:
    def __init__(self):
        self.db = DB()  # Usamos la base de datos local

    def create_task(self, name, created_by):
        task = {
            "estatus": 1,               # 1 = pendiente, 0 = completada
            "nombre de la tarea": name,              # nombre de la tarea
            "progreso": 0,             # progreso de la tarea (0 a 100)
            "creado por": created_by,  # quien creó la tarea
            "fecha de creación": datetime.now().isoformat() # fecha y hora de creación
        }
        return self.db.insert(task) # retorno insertando la tarea en la base de datos
    
    def get_task(self, index): # obtener tarea por índice
        try:
            return self.db.get(index) # retorno la tarea
        except IndexError:
            return None

    def update_task(self, index, name=None, status=None, progress=None): # actualizar tarea por índice
        task = self.get_task(index)
        if task:
            if name is not None: # si se proporciona un nuevo nombre, se actualiza
                task["nombre de la tarea"] = name
            if status is not None: # si se proporciona un nuevo estado, se actualiza
                task["estatus"] = status 
            if progress is not None: # si se proporciona un nuevo progreso, se actualiza
                if progress == 100:
                    task["estatus"] = 0
                else:
                    task["estatus"] = 1
                task["progreso"] = progress
            self.db.update(index, task)
            return task # retorno la tarea actualizada

    def delete_task(self, index): # eliminar tarea por índice
        try:
            self.db.delete(index) # elimino la tarea
        except IndexError:
            pass # Falla silenciosamente si el índice es inválido

    def list_tasks(self):
        return self.db.getAll() # retorno todas las tareas en la base de datos
