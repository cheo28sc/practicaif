empleados = []
clientes = []
trabajos = []
from colorama import Fore
from termcolor import colored


def menu_principal():
    while True:
        
        
        print(Fore.RED +" ------------------------------")
        print(colored( "|****** MENÚ PRINCIPAL ******  |  ", "red", attrs=["bold"]))
        print(Fore.RED +" ------------------------------")
        
        print(Fore.BLUE +" ---------------------")
        print(colored( "| MARIDOS DE ALQUILER |", "red", attrs=["bold"]))
        print(Fore.BLUE +" ---------------------")
        
        
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
            print(colored("Saliendo del programa...\
                    ESTA SEGURO QUE QUIERE SALIR DEL PROGRAMA? INGRESE A LA OPCION 4", "white", attrs=["bold"]))
            break
        else:
            print(Fore.RED +"Opción inválida.")
            # Función para mostrar el menú de empleados
def menu_empleados():
    while True:
        
        print(Fore.CYAN +" ---------------------------------")
        print(colored("|******* MENÚ DE EMPLEADOS *******|", "green", attrs=["bold"]))
        print(Fore.CYAN +" ---------------------------------")
        
        print(" ----------------------")
        print(Fore.GREEN + "| 1. Ingresar Empleado |")
        print("| 2. Borrar Empleado   |")
        print("| 3. Ver Empleados     |")
        print("| 4. Salir             |")
        print(" ----------------------")
        opcion = input("Ingrese una Opción: ")
        if opcion == "1":
            ingresar_empleado()
        elif opcion == "2":
            borrar_empleado()
        elif opcion == "3":
            ver_empleados()
        elif opcion == "4":
            break
        else:
            print(Fore.RED +"Opción Inválida.")

# Funciones para el módulo de empleados
def ingresar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    especialidad = input("Ingrese la especialidad del empleado: ")
    sexo = input("Ingrese el sexo del empleado: ")
    nuevo_empleado = {"nombre": nombre, "especialidad": especialidad, "sexo": sexo}
    if nuevo_empleado in empleados:
        print(Fore.RED +"Este empleado ya existe en la lista.")
    else:
        empleados.append(nuevo_empleado)
        print(Fore.RED +"Empleado Agregado con Éxito.")

def borrar_empleado():
    nombre = input("Ingrese el nombre del empleado que desea borrar: ")
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            empleados.remove(empleado)
            print(Fore.RED +"Empleado Eliminado con Éxito.")
            return
    print(Fore.RED +"No se Encontró un Empleado con ese Nombre.")

def ver_empleados():
    if empleados:
        for empleado in empleados:
                print(f"Nombre: {empleado['nombre']}\nEspecialidad: {empleado['especialidad']}\nSexo: {empleado['sexo']}\n")
    else:
        print(Fore.RED +"No hay empleados en la lista.")
# Función para mostrar el menú de clientes
def menu_clientes():
    while True:
        print(Fore.YELLOW +" --------------------------------")
        print(colored("|******* MENÚ DE CLIENTES *******|", "cyan", attrs=["bold"]))
        print(Fore.YELLOW +" --------------------------------")
        
        print(" ----------------------")
        print("| 1. Ingresar Cliente  |")
        print("| 2. Modificar Cliente |")
        print("| 3. Ver Clientes      |")
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
            print(Fore.RED +"Opción Inválida.")     
        
    

# Funciones para el módulo de clientes
def ingresar_cliente():
    nombre = input("Ingrese el Nombre del Cliente: ")
    apellido = input("Ingrese el Apellido del Cliente: ")
    cedula = input("Ingrese la Cédula del Cliente: ")
    telefono = input("Ingrese el Teléfono del Cliente: ")
    nuevo_cliente = {"nombre": nombre, "cedula": cedula, "telefono": telefono, "apellido": apellido,}
    for i, cliente in enumerate(clientes):
        if cliente["nombre"] > nombre:
            clientes.insert(i, nuevo_cliente)
            print(Fore.RED +"Cliente Agregado con Éxito.")
            return
    clientes.append(nuevo_cliente)
    print(Fore.RED +"Cliente Agregado con Éxito.")

def modificar_cliente():
    nombre = input("Ingrese el Nombre del Cliente que desea Modificar: ")
    for cliente in clientes:
        if cliente["nombre"] == nombre:
            cliente["cedula"] = input("Ingrese la nueva Cédula del Cliente: ")
            cliente["telefono"] = input("Ingrese el nuevo Teléfono del Cliente: ")
            print("Cliente modificado con éxito.")
            return
    print(Fore.RED +"No se Encontró un Cliente con ese Nombre.")

def ver_clientes():
    if clientes:
        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']}\nCédula: {cliente['cedula']}\nTeléfono: {cliente['telefono']}\n")
    else:
        print("No hay Clientes en la Lista.")
        # Función para mostrar el menú de trabajos
def menu_trabajos():
    while True:
        print(Fore.MAGENTA+" --------------------------------")
        print(colored("|******* MENÚ DE TRABAJOS *******|", "green", attrs=["bold"]))
        print(Fore.MAGENTA+" --------------------------------")
        
        print(" ----------------------------")
        print("| 1. Brindar Servicio        |")
        print("| 2. Ver Servicios Brindados |")
        print("| 3. Empleado Disponible     |")
        print("| 4. Salir                   |")
        print(" ----------------------------")
        opcion = input("Ingrese una Opción: ")
        if opcion == "1":
            brindar_servicio()
        elif opcion == "2":
            ver_servicios_brindados()
        elif opcion == "3":
            empleado_disponible()
        elif opcion == "4":
            break
        else:
            print(Fore.RED +"Opción Inválida.")
# Función para brindar un servicio
def brindar_servicio():
    print("Brindar servicio:")
    cliente_nombre = input("Ingrese el Nombre del Cliente: ")
    servicio = input("Ingrese el Servicio a Brindar: ")
    fecha = input("Ingrese la Fecha del Trabajo (en formato dd/mm/yyyy): ")

    empleado_disponible = True # Se asume que el empleado está disponible inicialmente
    for cliente in clientes:
        if cliente["nombre"] == cliente_nombre:
            for empleado in empleados:
                if empleado["especialidad"] == servicio:
                    # Verificar si el empleado ya está ocupado en otra tarea en la misma fecha
                    for trabajo in trabajos:
                        if trabajo["empleado"] == empleado["nombre"] and trabajo["fecha"] == fecha:
                            empleado_disponible = False
                            print(Fore.RED + f"El Empleado {empleado['nombre']} está ocupado en otra tarea en la misma fecha.")
                            break
                    if empleado_disponible:
                        print(f"El Empleado {empleado['nombre']} Brindará el servicio al Cliente {cliente['nombre']} el {fecha}  .")
                        trabajos.append({"cliente": cliente, "empleado": empleado, "servicio": servicio, "fecha": fecha})
                    return
            print(Fore.RED + "No hay Empleados Disponibles para Brindar ese Servicio.")
            return
    print(Fore.RED + "No se Encontró un Cliente con ese Nombre.")
from datetime import datetime

# Función para verificar si un empleado está disponible
def empleado_disponible():
    especialidad = input("Ingrese la Especialidad del Empleado que Busca: ")
    fecha = input("Ingrese la Fecha que Requiere (en formato dd/mm/yyyy): ")
    fecha = datetime.strptime(fecha, '%d/%m/%Y')
    empleado_disponible = None
    for empleado in empleados:
        if empleado["especialidad"] == especialidad:
            ocupado = False
            for trabajo in trabajos:
                if trabajo["empleado"] == empleado["nombre"] and datetime.strptime(trabajo["fecha"], '%d/%m/%Y') == fecha:
                    ocupado = True
                    break
            if not ocupado:
                empleado_disponible = empleado["nombre"]
                break
                
    if empleado_disponible:
        print(f"El empleado {empleado_disponible} está disponible para trabajar en esa especialidad en la fecha {fecha.strftime('%d/%m/%Y')}.")
    else:
        print(Fore.RED +"No se encontró un empleado con esa especialidad disponible en la fecha indicada.")
def ver_servicios_brindados():
    if trabajos:
        for trabajo in trabajos:
            print(f"Cliente: {trabajo['cliente']}\nServicio: {trabajo['servicio']}\nEmpleado: {trabajo['empleado']}\n")
    else:
        print(Fore.RED +"No hay Servicios Brindados.")
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
    opcion = input("Ingrese una Opción: ")
    if opcion == "1":
        menu_empleados()
    elif opcion == "2":
        menu_clientes()
    elif opcion == "3":
        menu_trabajos()
    elif opcion == "4":
        break
    else:
        print(Fore.RED +"Opción Inválida.")



