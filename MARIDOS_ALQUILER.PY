# Definición de listas vacías para almacenar los datos

empleados = []
clientes = []
trabajos = []
from colorama import Fore, Back, Style
def menu_principal():
    while True:
        from colorama import Fore, Back, Style    

        

        print(Fore.RED + "| Menú principal: |")
        print(" ---------------------")
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
            print("Opción inválida.")
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
            print("Opción inválida.")

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
    print("No se encontró un empleado con ese nombre.")

def ver_empleados():
    if empleados:
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}\nEspecialidad: {empleado['especialidad']}\nSexo: {empleado['sexo']}\n")
    else:
        print("No hay empleados en la lista.")
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
            print("Opción inválida.")     
        
    

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
    print("Cliente agregado con éxito.")

def modificar_cliente():
    nombre = input("Ingrese el nombre del cliente que desea modificar: ")
    for cliente in clientes:
        if cliente["nombre"] == nombre:
            cliente["cedula"] = input("Ingrese la nueva cédula del cliente: ")
            cliente["telefono"] = input("Ingrese el nuevo teléfono del cliente: ")
            print("Cliente modificado con éxito.")
            return
    print("No se encontró un cliente con ese nombre.")

def ver_clientes():
    if clientes:
        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']}\nCédula: {cliente['cedula']}\nTeléfono: {cliente['telefono']}\n")
    else:
        print("No hay clientes en la lista.")
        # Función para mostrar el menú de trabajos
def menu_trabajos():
    while True:
        print(" ----------------------------")
        print(Fore.LIGHTMAGENTA_EX +"|   Menú de trabajos:        |")
        print(" ----------------------------")
        
        print(" ----------------------------")
        print("| 1. Brindar servicio        |")
        print("| 2. Ver servicios brindados |")
        print("| 3. Empleado disponible     |")
        print("| 4. Salir                   |")
        print(" ----------------------------")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            brindar_servicio()
        elif opcion == "2":
            ver_servicios_brindados()
        elif opcion == "3":
            empleado_disponible()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Funciones para el módulo de trabajos
def brindar_servicio():
    print("Brindar servicio:")
    cliente_nombre = input("Ingrese el nombre del cliente: ")
    servicio = input("Ingrese el servicio a brindar: ")
    fecha = input("Ingrese la fecha del trabajo (en formato dd/mm/yyyy): ")
    for cliente in clientes:
        if cliente["nombre"] == cliente_nombre:
            for empleado in empleados:
                if empleado["especialidad"] == servicio:
                    print(f"El empleado {empleado['nombre']} brindará el servicio al cliente {cliente['nombre']} En la fecha {fecha['fecha']} .")
                    trabajos.append({"cliente": cliente, "empleado": empleado, "servicio": servicio, "fecha": fecha})
                    return
            print("No hay empleados disponibles para brindar ese servicio.")
            return
    print("No se encontró un cliente con ese nombre.")


# Función para ver los servicios brindados
def ver_servicios_brindados():
    if trabajos:
        for trabajo in trabajos:
            print(f"Cliente: {trabajo['cliente']}\nServicio: {trabajo['servicio']}\nEmpleado: {trabajo['empleado']}\n")
    else:
        print("No hay servicios brindados.")




# Función para verificar si un empleado está disponible
def empleado_disponible():
    especialidad = input("Ingrese la especialidad del empleado que busca: ")
    empleado_disponible = None
    for empleado in empleados:
        if empleado["especialidad"] == especialidad:
            ocupado = False
            for trabajo in trabajos:
                if trabajo["empleado"] == empleado["nombre"]:
                    ocupado = True
                    break
            if not ocupado:
                empleado_disponible = empleado["nombre"]
                break
                
    if empleado_disponible:
        print(f"El empleado {empleado_disponible} está disponible para trabajar en esa especialidad.")
    else:
        print("No se encontró un empleado con esa especialidad o todos los empleados están ocupados.")

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
        print("Opción inválida.")



