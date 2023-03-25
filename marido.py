

# Funciones para manejar la información de los empleados
def empleado():
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

# Funciones para manejar la información de los clientes
def agregar_cliente():
    nombre = input("Ingrese el nombre completo del cliente: ")
    identificacion = input("Ingrese el número de identificación del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    cliente = {"nombre": nombre, "identificacion": identificacion, "telefono": telefono}
    clientes.append(cliente)
    guardar_datos()
    print("Cliente agregado con éxito.")

def modificar_cliente():
    identificacion = input("Ingrese el número de identificación del cliente a modificar: ")
    for cliente in clientes:
        if cliente["identificacion"] == identificacion:
            cliente["nombre"] = input("Ingrese el nuevo nombre completo del cliente: ")
            cliente["identificacion"] = input("Ingrese la nueva identificacion del cliente: ")
            cliente["telefono"] = input("Ingrese el nuevo número de teléfono del cliente: ")
            guardar_datos()
            print("Cliente modificado con éxito.")
            return
    print("Cliente no encontrado.")

def ver_clientes():
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']}, Identificación: {cliente['identificacion']}, Dirección: {cliente['direccion']}, Teléfono: {cliente['telefono']}")

# Funciones para manejar la información de los trabajos
def asignar_trabajo():
    
    numero = len(trabajos) + 1
    servicio  = input("Ingrese la descripción del trabajo: ")
    cliente = input("Ingrese el número de identificación del cliente para el trabajo: ")
    empleado = input("Ingrese el número de identificación del empleado para el trabajo: ")
    fecha_inicio = input("Ingrese la fecha de inicio del trabajo (dd/mm/yyyy): ")
    fecha_fin = input("Ingrese la fecha de finalización del trabajo (dd/mm/yyyy): ")
    trabajo = {"numero": numero, "servicio": servicio, "cliente": cliente, "empleado": empleado, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin}
    trabajos.append(trabajo)
    guardar_datos()
    print("Trabajo asignado con éxito.")
while True:
    print("1. Empleado.")
    print("2. Clientes.")
    print("3. Trabajos.")
    print("5. Salir.")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        nombre, especialidad, sexo = agregar_empleado()
        print(f"Nombre: {nombre}")
        print(f"Especialidad: {especialidad}")
        print(f"Sexo: {sexo}")
    
    elif opcion == 2:
        nombre_cliente, cedula, telefono = agregar_cliente()
        print(f"Nombre del cliente: {nombre_cliente}")
        print(f"Cedula: {cedula}")
        print(f"Telefono: {telefono}")
    elif opcion == 3:
        for curso in cursos:
            promedio = calcular_promedio(curso)
            print(f"El promedio de {curso} es {promedio:.2f}")
    elif opcion == 4:
        total, total_con_descuento, descuento = calcular_total_pagar(cursos)
        facturar_cursos(total, total_con_descuento, descuento)
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Intente de nuevo.")





