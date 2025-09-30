import os
import json
from uuid import uuid4

class DB():

    def _getLocalDB(self):
        try:
            db_file = open(f'{self._dbPath}\\local_db.json', 'r', encoding='utf8') # Abrir archivo en modo lectura
            data = json.load(db_file)
            db_file.close()
            return data
        except:
            return None

    def _updateLocalDB(self):
        try:
            db_file = open(f'{self._dbPath}\\local_db.json', 'w', encoding='utf8') # Crear o abrir archivo en modo escritura
            json.dump(self._db, db_file, indent=4)
            db_file.close()
        except:
            print("[DB] Se produjo un error el proceso de actualización.")

    def __init__(self):
        self._dbPath = os.path.dirname(os.path.abspath(__file__))

        local_db = self._getLocalDB()
        if local_db != None:
            self._db = local_db
            print("[DB] Obtenida correctamente.")
        else:
            self._db = []
            self._updateLocalDB()
            print("[DB] Creada correctamente.")

    def insert(self, element):
        if (isinstance(element, dict)):
            data = {'uid': str(uuid4())} | element
            self._db.append(data)
            self._updateLocalDB()
            return data
        else:
            print("[DB] ERROR: Solo se permiten diccionarios para el método insert")

    def get(self, index):
        return self._db[index]

    def update(self, index, data):
        self._db[index] = data
        self._updateLocalDB()

    def delete(self, index):
        del self._db[index]
        self._updateLocalDB()
    
    def clear(self):
        self._db = []
        self._updateLocalDB()
    
    def __str__(self):
        return str(self._db)
