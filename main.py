"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file

try:
    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
    else:
        ruta_f = sys.argv[1]
        tareas = read_todo_file(ruta_f)

        i = 2
        while i < len(sys.argv):
            comando = sys.argv[i]

            if comando == "view":
                print("Tasks:")
                for tarea in tareas:
                    print(tarea)
                i += 1

            elif comando == "add":
                try:
                    nueva_tarea = sys.argv[i+1]
                    tareas.append(nueva_tarea)
                    print(f'Task "{nueva_tarea}" added.')
                    i += 2
                except IndexError:
                    print('Task description required for "add".')
                    i += 1

            elif comando == "remove":
                try:
                    tarea_e = sys.argv[i+1]
                    if tarea_e in tareas:
                        tareas.remove(tarea_e)
                        print(f'Task "{tarea_e}" removed.')
                    else:
                        print(f'Task "{tarea_e}" not found.')
                    i += 2
                except IndexError:
                    print('Task description required for "remove".')
                    i += 1

            else:
                raise ValueError("Command not found!")

        with open(ruta_f, "w") as file:
            for tarea in tareas:
                file.write(tarea + "\n")

except IndexError:
    print("Insufficient arguments provided!")
except ValueError as e:
    print(e)
except FileNotFoundError:
    print(f"File {sys.argv[1]} not found! Returning an empty to-do list.")