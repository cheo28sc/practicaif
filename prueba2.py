empleados = []
clientes = []
trabajos = []
from colorama import Fore
from termcolor import colored
def menu_principal():
    while True:
        from colorama import Fore   
        from termcolor import colored
        
        print(Fore.RED +" -----------------")
        print(colored( "| Menú principal  |", "red", attrs=["bold"]))
        print(" -----------------")
        
        print(Fore.BLUE +" ---------------------")
        print(Fore.BLUE + "| Maridos de Alquiler |")
        print(" ---------------------")
        
        
        print(" ---------------------")
        print("|     1. Empleados    |")
        print("|     2. Clientes     |")
        print("|     3. Trabajos     |")
        print("|     4. Salir        |")
        print(" ---------------------")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            menu_empleados()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_trabajos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print(Fore.RED +"Opción inválida.")
            # Función para mostrar el menú de empleados
def menu_empleados():
    while True:
        print(" ----------------------")
        print(Fore.CYAN +"|   Menú de empleados: |")
        print(" ----------------------")
        
        print(" ----------------------")
        print(Fore.GREEN + "| 1. Ingresar empleado |")
        print("| 2. Borrar empleado   |")
        print("| 3. Ver empleados     |")
        print("| 4. Salir             |")
        print(" ----------------------")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            ingresar_empleado()
        elif opcion == "2":
            borrar_empleado()
        elif opcion == "3":
            ver_empleados()
        elif opcion == "4":
            break
        else:
            print(Fore.RED +"Opción inválida.")

# Funciones para el módulo de empleados
def ingresar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    especialidad = input("Ingrese la especialidad del empleado: ")
    sexo = input("Ingrese el sexo del empleado: ")
    nuevo_empleado = {"nombre": nombre, "especialidad": especialidad, "sexo": sexo}
    if nuevo_empleado in empleados:
        print("Este empleado ya existe en la lista.")
    else:
        empleados.append(nuevo_empleado)
        print("Empleado agregado con éxito.")

def borrar_empleado():
    nombre = input("Ingrese el nombre del empleado que desea borrar: ")
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            empleados.remove(empleado)
            print("Empleado eliminado con éxito.")
            return
    print(Fore.RED +"No se encontró un empleado con ese nombre.")

def ver_empleados():
    if empleados:
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}\nEspecialidad: {empleado['especialidad']}\nSexo: {empleado['sexo']}\n")
    else:
        print(Fore.RED +"No hay empleados en la lista.")
# Función para mostrar el menú de clientes
def menu_clientes():
    while True:
        print(" ----------------------")
        print(Fore.LIGHTYELLOW_EX +"| Menú de clientes:    |")
        print(" ----------------------")
        
        print(" ----------------------")
        print("| 1. Ingresar cliente  |")
        print("| 2. Modificar cliente |")
        print("| 3. Ver clientes      |")
        print("| 4. Salir             |")
        print(" ----------------------")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            modificar_cliente()
        elif opcion == "3":
            ver_clientes()
        elif opcion == "4":
            break
        else:
            print(Fore.RED +"Opción inválida.")     
        
    

# Funciones para el módulo de clientes
def ingresar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    nuevo_cliente = {"nombre": nombre, "cedula": cedula, "telefono": telefono, "apellido": apellido,}
    for i, cliente in enumerate(clientes):
        if cliente["nombre"] > nombre:
            clientes.insert(i, nuevo_cliente)
            print("Cliente agregado con éxito.")
            return
    clientes.append(nuevo_cliente)
    print(Fore.RED +"Cliente agregado con éxito.")

def modificar_cliente():
    nombre = input("Ingrese el nombre del cliente que desea modificar: ")
    for cliente in clientes:
        if cliente["nombre"] == nombre:
            cliente["cedula"] = input("Ingrese la nueva cédula del cliente: ")
            cliente["telefono"] = input("Ingrese el nuevo teléfono del cliente: ")
            print("Cliente modificado con éxito.")
            return
    print(Fore.RED +"No se encontró un cliente con ese nombre.")

def ver_clientes():
    if clientes:
        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']}\nCédula: {cliente['cedula']}\nTeléfono: {cliente['telefono']}\n")
    else:
        print("No hay clientes en la lista.")
        # Función para mostrar el menú de trabajos


def brindar_servicio():
    print("Brindar servicio:")
    nombre = input("Ingrese el nombre del trabajo: ")
    descripcion = input("Ingrese la descripción del trabajo: ")
    fecha_inicio = input("Ingrese la fecha de inicio del trabajo (DD/MM/AAAA): ")
    fecha_fin = input("Ingrese la fecha de fin del trabajo (DD/MM/AAAA): ")
    cliente = input("Ingrese el nombre del cliente: ")
    empleado = input("Ingrese el nombre del empleado asignado al trabajo: ")
    for cliente in clientes:
        if cliente["nombre"] == nombre:
            for empleado in empleados:
                if empleado["especialidad"] == servicio:
                    print(f"El empleado {empleado['nombre']} brindará el servicio al cliente {cliente['nombre']} el {fecha}  .")
    trabajos.append ({"cliente": cliente, "empleado": empleado, "servicio": servicio, "fecha": fecha})
    print("Trabajo agregado con éxito.")

def modificar_trabajo():
    nombre = input("Ingrese el nombre del trabajo que desea modificar: ")
    for trabajo in trabajos:
        if trabajo["nombre"] == nombre:
            trabajo["descripcion"] = input("Ingrese la nueva descripción del trabajo: ")
            trabajo["fecha_inicio"] = input("Ingrese la nueva fecha de inicio del trabajo (DD/MM/AAAA): ")
            trabajo["fecha_fin"] = input("Ingrese la nueva fecha de fin del trabajo (DD/MM/AAAA): ")
            trabajo["cliente"] = input("Ingrese el nuevo nombre del cliente: ")
            trabajo["empleado"] = input("Ingrese el nuevo nombre del empleado asignado al trabajo: ")
            print("Trabajo modificado con éxito.")
            return
    print(Fore.RED +"No se encontró un trabajo con ese nombre.")

def ver_trabajos():
    if trabajos:
        for trabajo in trabajos:
            print(f"Nombre: {trabajo['nombre']}\nDescripción: {trabajo['descripcion']}\nFecha de inicio: {trabajo['fecha_inicio']}\nFecha de fin: {trabajo['fecha_fin']}\nCliente: {trabajo['cliente']}\nEmpleado asignado: {trabajo['empleado']}\n")
    else:
        print(Fore.RED +"No hay trabajos en la lista.")


menu_principal()
empleados = []
clientes = []
trabajos = []
while True:
    print("Menú principal:")
    print(" ---------------------")
    print("| Maridos de Alquiler |")
    print(" ---------------------")
    print("1. Empleados")
    print("2. Clientes")
    print("3. Trabajos")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        menu_empleados()
    elif opcion == "2":
        menu_clientes()
    elif opcion == "3":
        menu_trabajos()
    elif opcion == "4":
        break
    else:
        print(Fore.RED +"Opción inválida.")






