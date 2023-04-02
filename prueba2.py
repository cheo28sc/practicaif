empleados = []
clientes = []
trabajos = []
from colorama import Fore
from termcolor import colored
import datetime
from datetime import datetime

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
import datetime
from termcolor import colored, cprint

# Definición de listas vacías para almacenar los datos
clientes = []
empleados = []
trabajos = []

# Función para mostrar el menú de trabajos
def menu_trabajos():
    while True:
        cprint(" --------------------------------", "magenta")
        cprint("|******* MENÚ DE TRABAJOS *******|", "green", attrs=["bold"])
        cprint(" --------------------------------", "magenta")

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
            cprint("Opción Inválida.", "red")

# Función para brindar un servicio
def brindar_servicio():
    print("Brindar servicio:")
    cliente_nombre = input("Ingrese el Nombre del Cliente: ")
    servicio = input("Ingrese el Servicio a Brindar: ")
    fecha = input("Ingrese la Fecha del Trabajo (en formato dd/mm/yyyy): ")
    hora_inicio = datetime.datetime.strptime(input("Ingrese la Hora de Inicio del Trabajo (en formato hh:mm): "), '%H:%M')

    hora_fin_dt = hora_inicio + datetime.timedelta(hours=3)
    hora_fin = hora_fin_dt.strftime('%H:%M')
    for cliente in clientes:
        if cliente["nombre"] == cliente_nombre:
            for empleado in empleados:
                if empleado["especialidad"] == servicio:
                    disponible = True
                    for trabajo in trabajos:
                        if trabajo["empleado"] == empleado and \
                            trabajo["fecha"] == fecha and \
                            (hora_inicio <= trabajo["hora_fin_dt"] and hora_fin_dt >= trabajo["hora_inicio_dt"]):
                            disponible = False
                            break
                    if disponible:
                        print(f"El Empleado {empleado['nombre']} Brindará el servicio al Cliente {cliente['nombre']} el {fecha} de {hora_inicio.strftime('%H:%M')} a {hora_fin}.")
                        trabajos.append({"cliente": cliente, "empleado": empleado, "servicio": servicio, "fecha": fecha, "hora_inicio": hora_inicio.strftime('%H:%M'), "hora_fin": hora_fin, "hora_inicio_dt": hora_inicio, "hora_fin_dt": hora_fin_dt})
                        return
    cprint("No se encontró un Cliente o Empleado con esa información.", "red")

# Función para ver los servicios brindados
def ver_servicios_brindados():
    if trabajos:
        for trabajo in trabajos:
            inicio = datetime.datetime.strptime(trabajo["hora_inicio"], '%H:%M')
            fin = datetime.datetime.strptime(trabajo["hora_fin"], '%H:%M')
            duracion = (fin - inicio).total_seconds() / 3600  # calcula duración en horas
            if duracion == 3:
                print(f"Cliente: {trabajo['cliente']['nombre']}\nServicio: {trabajo['servicio']}\nEmpleado: {trabajo['empleado']['nombre']}\nInicio: {inicio.strftime('%H:%M')}\nFin: {fin.strftime('%H:%M')}\n")

def empleado_disponible():
    especialidad = input("Ingrese la Especialidad del Empleado que Busca: ")
    hora_inicio = datetime.datetime.strptime(input("Ingrese la Hora de Inicio del Trabajo (en formato HH:MM): "), "%H:%M")
    hora_fin = hora_inicio + datetime.timedelta(hours=3)
    
    empleado_disponible = None
    for empleado in empleados:
        if empleado["especialidad"] == especialidad:
            ocupado = False
            for trabajo in trabajos:
                if trabajo["empleado"] == empleado and \
                        trabajo["fecha"] == fecha and \
                        (hora_inicio <= trabajo["hora_fin_dt"] and hora_fin >= trabajo["hora_inicio_dt"]):
                    ocupado = True
                    break
            if not ocupado:
                empleado_disponible = empleado["nombre"]
                break
                
    if empleado_disponible:
        print(f"El empleado {empleado_disponible} está disponible para trabajar en esa especialidad y horario.")
    else:
        print(Fore.RED +"No se encontró un Empleado con esa Especialidad o todos los Empleados están Ocupados en ese horario.")
        

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



