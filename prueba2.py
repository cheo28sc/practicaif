# Lista de empleados
empleados = []

# Lista de clientes
clientes = []

# Lista de trabajos
trabajos = []

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
            print("Saliendo del programa...")
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

# Función para ingresar un empleado
def ingresar_empleado():
    print("Ingresar empleado:")
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    especialidad = input("Ingrese la especialidad del empleado: ")
    sexo = input = ("Ingrese el Sexo")
    empleados.append((nombre, apellido, edad, especialidad, sexo))
    print("Empleado ingresado correctamente.")

# Función para borrar un empleado
def borrar_empleado():
    print("Borrar empleado:")
    apellido = input("Ingrese el apellido del empleado a borrar: ")
    for empleado in empleados:
        if empleado[1] == apellido:
            empleados.remove(empleado)
            print("Empleado borrado correctamente.")
            return
    print("Empleado no encontrado.")

# Función para ver los empleados
def ver_empleados():
    print("Lista de empleados:")
    for empleado in empleados:
        print(f"{empleado[0]} {empleado[1]}, {empleado[2]} años, Teléfono: {empleado[3]}")

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
            ver_clientes()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Función para ingresar un cliente
# Función para ingresar un cliente
def ingresar_cliente():
    print("Ingresar cliente:")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    telefono = input("Ingrese el teléfono del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    clientes.append((nombre, apellido, edad, telefono, direccion))
    print("Cliente ingresado correctamente.")

# Función para modificar un cliente
def modificar_cliente():
    print("Modificar cliente:")
    apellido = input("Ingrese el apellido del cliente a modificar: ")
    for cliente in clientes:
        if cliente[1] == apellido:
            nombre = input(f"Ingrese el nuevo nombre para {cliente[0]} {cliente[1]}: ")
            edad = int(input(f"Ingrese la nueva edad para {cliente[0]} {cliente[1]}: "))
            telefono = input(f"Ingrese el nuevo teléfono para {cliente[0]} {cliente[1]}: ")
            direccion = input(f"Ingrese la nueva dirección para {cliente[0]} {cliente[1]}: ")
            clientes.remove(cliente)
            clientes.append((nombre, apellido, edad, telefono, direccion))
            print("Cliente modificado correctamente.")
            return
    print("Cliente no encontrado.")

# Función para ver los clientes
def ver_clientes():
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"{cliente[0]} {cliente[1]}, {cliente[2]} años, Teléfono: {cliente[3]}, Dirección: {cliente[4]}")

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

# Función para brindar un servicio
def brindar_servicio():
    print("Brindar servicio:")
    cliente_apellido = input("Ingrese el apellido del cliente: ")
    servicio = input("Ingrese el servicio a brindar: ")
    for cliente in clientes:
        if cliente[1] == cliente_apellido:
            empleado_apellido = input("Ingrese el apellido del empleado: ")
            for empleado in empleados:
                if empleado[1] == empleado_apellido:
                    trabajos.append((cliente, empleado, servicio))
                    print("Servicio brindado correctamente.")
                    return
            print("Empleado no encontrado.")
            return
    print("Cliente no encontrado.")

# Función para ver los servicios brindados
def ver_servicios_brindados():
    print("Servicios brindados:")
    for trabajo in trabajos:
        print(f"Cliente: {trabajo[0][0]} {trabajo[0][1]}, Empleado: {trabajo[1][0]} {trabajo[1][1]}, Servicio: {trabajo[2]}")

# Función para verificar si un empleado está disponible
# Función para verificar si un empleado está disponible
def empleado_disponible():
    apellido = input("Ingrese el apellido del empleado: ")
    for empleado in empleados:
        if empleado[1] == apellido:
            disponible = True
            for trabajo in trabajos:
                if trabajo[1][1] == apellido:
                    disponible = False
                    print(f"{empleado[0]} {empleado[1]} no está disponible.")
                    break
            if disponible:
                print(f"{empleado[0]} {empleado[1]} está disponible.")
            return
    print("Empleado no encontrado.")
empleados = []
clientes = []
trabajos = []

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


