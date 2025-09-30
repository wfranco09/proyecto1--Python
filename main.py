#codigo de prueba estandar 
""""from adm_tareas import TaskManager 

tm = TaskManager()  # TaskManager usa DB internamente

# Crear tareas
tm.create_task("Example", "Luis")

# Listar tareas
print(tm.list_tasks())

# Actualizar tarea
tm.update_task(0, status=0, progress=50)

# Obtener tarea específica
print(tm.get_task(0)['uid'])

# Eliminar tarea
tm.delete_task(0)

# Limpiar todas las tareas desde la DB directamente
tm.db.clear()
print(tm.list_tasks()) """

# Interfaz de línea de comandos para el gestor de tareas (consola)

from adm_tareas import TaskManager
def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Actualizar tarea")
    print("4. Eliminar tarea")
    print("5. Limpiar todas las tareas")
    print("6. Salir")

def main():
    tm = TaskManager()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            creador = input("Creado por: ")
            tarea = tm.create_task(nombre, creador)
            print(f"Tarea creada: {tarea}")

        elif opcion == "2":
            tareas = tm.list_tasks()
            if not tareas:
                print("No hay tareas.")
            for i, t in enumerate(tareas):
                print(f"{i}: {t}")

        elif opcion == "3":

            index = int(input("Índice de la tarea a actualizar: "))
            nombre = input("Nuevo nombre (Enter para no cambiar): ")
            status = input("Nuevo estado (1=pendiente, 0=completada, Enter para no cambiar): ")
            progress = input("Nuevo progreso (0-100, Enter para no cambiar): ")

            # Convertir valores si se ingresaron
            status = int(status) if status else None
            progress = int(progress) if progress else None
            nombre = nombre if nombre else None

            tarea_actualizada = tm.update_task(index, name=nombre, status=status, progress=progress)
            if tarea_actualizada:
                print(f"Tarea actualizada: {tarea_actualizada}")

        elif opcion == "4":
            index = int(input("Índice de la tarea a eliminar: "))
            tm.delete_task(index)
            print("Tarea eliminada.")

        elif opcion == "5":
            tm.db.clear()
            print("Todas las tareas han sido eliminadas.")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()


