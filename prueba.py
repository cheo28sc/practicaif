def agregar_empleado():
    nombre = input("Ingrese el nombre completo del empleado: ")
    especialidad = input("Ingrese la Especialidad : ")
    sexo = input("Ingrese ingrese el sexo: ")

    empleado = {"nombre": nombre, "especialidad": especialidad, "sexo": sexo,}
    empleado.append(empleado)
    guardar_datos()
    print("Empleado agregado con éxito.")

def borrar_empleado():
    nombre = input("Ingrese el nombre del empleado a borrar: ")
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            empleados.remove(empleado)
            guardar_datos()
            print("Empleado borrado con éxito.")
            return
    print("Empleado no encontrado.")

def ver_empleados():
    print("Lista de empleados:")
    for empleado in empleados:
        print(f"Nombre: {empleado['nombre']}, Especialidad: {empleado['especialidad']}, sexo: {empleado['sexo']}")
