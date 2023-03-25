def menu_principal():
    print("Menú principal:")
    print("1. Empleados")
    print("2. Clientes")
    print("3. Trabajos")
    print("4. Salir")

# Función para mostrar el menú de empleados
def menu_empleados():
    print("Menú de empleados:")
    print("1. Ingresar empleado")
    print("2. Borrar empleado")
    print("3. Ver empleados")
    print("4. Salir")

# Función para mostrar el menú de clientes
def menu_clientes():
    print("Menú de clientes:")
    print("1. Ingresar cliente")
    print("2. Modificar cliente")
    print("3. Ver clientes")
    print("4. Salir")

# Función para mostrar el menú de trabajos
def menu_trabajos():
    print("Menú de trabajos:")
    print("1. Brindar servicio")
    print("2. Ver servicios brindados")
    print("3. Empleado disponible")
    print("4. Salir")






# Definición de listas
empleados = []
clientes = []
trabajos = []

# Funciones para el módulo de empleados
def ingresar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    especialidad = input("Ingrese la especialidad del empleado: ")
    sexo = input("Ingrese el sexo del empleado: ")
    empleado = {"nombre": nombre, "especialidad": especialidad, "sexo": sexo}
    if not empleados:
        empleados.append(empleado)
    else:
        posicion = 0
        while posicion < len(empleados) and empleados[posicion]["nombre"] < nombre:
            posicion += 1
        if posicion < len(empleados) and empleados[posicion]["nombre"] == nombre:
            print("Error: ya existe un empleado con ese nombre")
        else:
            empleados.insert(posicion, empleado)
            print("Empleado ingresado correctamente")

def borrar_empleado():
    nombre = input("Ingrese el nombre del empleado a borrar: ")
    posicion = 0
    while posicion < len(empleados) and empleados[posicion]["nombre"] != nombre:
        posicion += 1
    if posicion == len(empleados):
        print("Error: no existe un empleado con ese nombre")
    else:
        del empleados[posicion]
        print("Empleado borrado correctamente")

def ver_empleados():
    if not empleados:
        print("No hay empleados registrados")
    else:
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}, Especialidad: {empleado['especialidad']}, Sexo: {empleado['sexo']}")

# Funciones para el módulo de clientes
def ingresar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = {"nombre": nombre, "cedula": cedula, "telefono": telefono}
    if not clientes:
        clientes.append(cliente)
    else:
        posicion = 0
        while posicion < len(clientes) and clientes[posicion]["nombre"] < nombre:
            posicion += 1
        if posicion < len(clientes) and clientes[posicion]["nombre"] == nombre:
            print("Error: ya existe un cliente con ese nombre")
        else:
            clientes.insert(posicion, cliente)
            print("Cliente ingresado correctamente")

def modificar_cliente():
    nombre = input("Ingrese el nombre del cliente a modificar: ")
    posicion = 0
    while posicion < len(clientes) and clientes[posicion]["nombre"] != nombre:
        posicion += 1
    if posicion == len(clientes):
        print("Error: no existe un cliente con ese nombre")
    else:
        cedula = input("Ingrese la nueva cédula del cliente: ")
        telefono = input("Ingrese el nuevo teléfono del cliente: ")
        clientes[posicion]["cedula"] = cedula
        clientes[posicion]["telefono"] = telefono
        print("Cliente modificado correctamente")

def ver_clientes():
    if not clientes:
        print("No hay clientes registrados")
    else:
        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']}, Cédula: {cliente['cedula']}, Teléfono: {cliente['telefono']}")

# Funciones para el módulo de trabajos
def menu_trabajos():
    while True:
        print("\n--- Menú de trabajos ---")
        print("1. Brindar servicio")
        print("2. Empleado disponible")
        print("3. Ver servicios brindados")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Brindar servicio
            print("\n--- Brindar servicio ---")
            cliente = input("Ingrese el nombre del cliente: ")
            empleado = input("Ingrese el nombre del empleado: ")
            servicio = input("Ingrese el nombre del servicio: ")
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
            
            # Verificar si el empleado está disponible
            if empleado in empleados_disponibles:
                # Agregar el trabajo a la lista de trabajos
                trabajos.append((fecha, cliente, servicio, empleado))
                
                # Cambiar el estado del empleado a no disponible
                empleados_disponibles.remove(empleado)
                
                print("El trabajo se ha registrado exitosamente.")
            else:
                print("Lo sentimos, el empleado no está disponible en este momento.")
                
        elif opcion == "2":
            # Empleado disponible
            print("\n--- Empleado disponible ---")
            empleado = input("Ingrese el nombre del empleado: ")
            
            # Verificar si el empleado está en la lista de empleados
            if empleado in empleados:
                # Verificar si el empleado está disponible
                if empleado in empleados_disponibles:
                    print("El empleado ya está disponible.")
                else:
                    empleados_disponibles.append(empleado)
                    print("El empleado ahora está disponible.")
            else:
                print("El empleado no existe en la lista.")
                
        elif opcion == "3":
            # Ver servicios brindados
            print("\n--- Servicios brindados ---")
            
            # Verificar si hay trabajos registrados
            if len(trabajos) > 0:
                print("Fecha\t\tCliente\t\tServicio\tEmpleado")
                print("--------------------------------------------------------------")
                
                for trabajo in trabajos:
                    print(f"{trabajo[0]}\t{trabajo[1]}\t{trabajo[2]}\t{trabajo[3]}")
            else:
                print("No hay servicios brindados registrados.")
                
        elif opcion == "4":
            # Salir
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")
