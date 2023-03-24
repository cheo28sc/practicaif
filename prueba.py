# Lista de empleados, clientes y trabajos
empleados = []
clientes = []
trabajos = []

# Funciones para el menú de empleados
def ingresar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    especialidad = input("Ingrese su especialidad: ")
    sexo = input("Ingrese su Sexo")
    empleados.append(nombre,especialidad,sexo)
    print("Empleado ingresado con éxito.")

def borrar_empleado():
    nombre = input("Ingrese el nombre del empleado a borrar: ")
    if nombre in empleados:
        empleados.remove(nombre)
        print("Empleado eliminado con éxito.")
    else:
        print("El empleado no se encontró en la lista.")

def ver_empleados():
    print("Lista de empleados:")
    for empleado in empleados:
        print("- " + empleado)

# Funciones para el menú de clientes
def ingresar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("ingrese el numero de cedula: ")
    telefono = input("ingresa el numero de telefono")
    clientes.append(nombre,cedula,telefono)
    print("Cliente ingresado con éxito.")

def modificar_cliente():
    nombre = input("Ingrese el nombre del cliente a modificar: ")
    if nombre in clientes:
        numero_cedula = input("Ingrese el nuevo nombre para el cliente: ")
        numero_telefono = input("Ingrese el nuevo numero de telefono")
        indice = clientes.index(nombre)
        clientes[indice] = numero_cedula
        clientes[indice] = numero_telefono
        print("Cliente modificado con éxito.")
    else:
        print("El cliente no se encontró en la lista.")

def ver_cliente():
    print("Lista de clientes:")
    for cliente in clientes:
        print("- " + cliente)

# Funciones para el menú de trabajos
def brindar_servicio():
    empleado = input("Ingrese el nombre del empleado que brindará el servicio: ")
    cliente = input("Ingrese el nombre del cliente: ")
    trabajo = (empleado, cliente)
    trabajos.append(trabajo)
    print("Servicio brindado con éxito.")

def ver_servicios_brindados():
    print("Lista de servicios brindados:")
    for trabajo in trabajos:
        print("- Empleado: " + trabajo[0] + " - Cliente: " + trabajo[1])

def empleado_disponible():
    print("Lista de empleados disponibles:")
    for empleado in empleados:
        if empleado not in [t[0] for t in trabajos]:
            print("- " + empleado)

# Función para mostrar el menú principal
def menu_principal():
    while True:
        print("Menú principal:")
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

# Función para mostrar el menú de empleados
def menu_empleados():
    while True:
        print("Menú de empleados:")
        print("1. Ingresar empleado")
        print("2. Borrar empleado")
        print("3. Ver empleados")
        print("4. Salir")
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

# Función para mostrar
# Función para mostrar el menú de clientes
def menu_clientes():
    while True:
        print("Menú de clientes:")
        print("1. Ingresar cliente")
        print("2. Modificar cliente")
        print("3. Ver clientes")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            modificar_cliente()
        elif opcion == "3":
            ver_cliente()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Función para mostrar el menú de trabajos
def menu_trabajos():
    while True:
        print("Menú de trabajos:")
        print("1. Brindar servicio")
        print("2. Ver servicios brindados")
        print("3. Empleado disponible")
        print("4. Salir")
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
# Llamada a la función menu_principal para iniciar el programa
menu_principal()
