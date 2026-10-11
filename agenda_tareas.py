tareas = []


def validar_entrada(texto):
    return texto.strip() != ""


def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")

    if not validar_entrada(descripcion):
        print("Error: la descripción no puede estar vacía.")
        return

    tarea = {
        "descripcion": descripcion.strip(),
        "completada": False
    }

    tareas.append(tarea)

    print("Tarea agregada correctamente.")


def mostrar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n--- LISTA DE TAREAS ---")

    for indice, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"

        print(f"{indice}. {tarea['descripcion']} - {estado}")


def completar_tarea():
    if not tareas:
        print("No hay tareas para completar.")
        return

    mostrar_tareas()

    try:
        numero = int(input("Ingrese el número de la tarea que desea completar: "))

        if numero < 1 or numero > len(tareas):
            print("Error: el número de tarea no es válido.")
            return

        tarea = tareas[numero - 1]

        if tarea["completada"]:
            print("Esta tarea ya está completada.")
            return

        tarea["completada"] = True

        print("Tarea marcada como completada.")

    except ValueError:
        print("Error: debe ingresar un número válido.")


def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        return

    mostrar_tareas()

    try:
        numero = int(input("Ingrese el número de la tarea que desea eliminar: "))

        if numero < 1 or numero > len(tareas):
            print("Error: el número de tarea no es válido.")
            return

        tarea_eliminada = tareas.pop(numero - 1)

        print(f"Tarea eliminada: {tarea_eliminada['descripcion']}")

    except ValueError:
        print("Error: debe ingresar un número válido.")


def mostrar_menu():
    print("\n==============================")
    print("      AGENDA DE TAREAS")
    print("==============================")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            completar_tarea()

        elif opcion == "4":
            eliminar_tarea()

        elif opcion == "5":
            print("Gracias por utilizar la Agenda de Tareas.")
            break

        else:
            print("Error: opción no válida. Seleccione una opción del 1 al 5.")


main()