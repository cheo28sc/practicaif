# Definición de las clases
class Empleado:
    def __init__(self, nombre, especialidad, sexo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.sexo = sexo
        self.disponible = True

class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

class Trabajo:
    def __init__(self, fecha, cliente, servicio, empleado):
        self.fecha = fecha
        self.cliente = cliente
        self.servicio = servicio
        self.empleado = empleado

# Definición de las listas
lista_empleados = []
lista_clientes = []
lista_trabajos = []

# Funciones del módulo cliente
def ingresar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese el número de cédula del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    cliente = Cliente(nombre, cedula, telefono)
    # Insertar cliente en orden en la lista enlazada
    if not lista_clientes:
        lista_clientes.append(cliente)
    else:
        for i, c in enumerate(lista_clientes):
            if c.cedula > cedula:
                lista_clientes.insert(i, cliente)
                break
        else:
            lista_clientes.append(cliente)
    print("Cliente ingresado correctamente.")

def modificar_cliente():
    cedula = input("Ingrese el número de cédula del cliente a modificar: ")
    for c in lista_clientes:
        if c.cedula == cedula:
            telefono = input("Ingrese el nuevo número de teléfono: ")
            c.telefono = telefono
            print("Cliente modificado correctamente.")
            break
    else:
        print("No se encontró ningún cliente con esa cédula.")

def ver_clientes():
    if lista_clientes:
        for c in lista_clientes:
            print("Nombre:", c.nombre)
            print("Cédula:", c.cedula)
            print("Teléfono:", c.telefono)
            print()
    else:
        print("No hay clientes registrados.")

# Funciones del módulo empleado
def ingresar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    especialidad = input("Ingrese la especialidad del empleado: ")
    sexo = input("Ingrese el sexo del empleado: ")
    empleado = Empleado(nombre, especialidad, sexo)
    # Insertar empleado en orden en la lista enlazada
    if not lista_empleados:
        lista_empleados.append(empleado)
    else:
        for i, e in enumerate(lista_empleados):
            if e.nombre > nombre:
                lista_empleados.insert(i, empleado)
                break
        else:
            lista_empleados.append(empleado)
    print("Empleado ingresado correctamente.")

def borrar_empleado():
    nombre = input("Ingrese el nombre del empleado a borrar: ")
    for e in lista_empleados:
        if e.nombre == nombre:
            if e.disponible:
                lista_empleados.remove(e)
                print("Empleado borrado correctamente.")
            else:
                print("El empleado no se puede borrar porque está en un trabajo.")
            break
    else:
        print("No se encontró ningún empleado con ese nombre.")

def ver_empleados():
    if empleados:
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}\nEspecialidad: {empleado['especialidad']}\nSexo: {empleado['sexo']}\n")
    else:
        print("No hay empleados en la lista.")


def brindar_servicio(empleados, clientes, trabajos):
    # Solicitar datos del servicio
    fecha = input("Ingrese la fecha del servicio (dd/mm/aaaa): ")
    cliente = input("Ingrese el nombre del cliente: ")
    servicio = input("Ingrese el nombre del servicio a realizar: ")
    empleado = input("Ingrese el nombre del empleado asignado: ")

    # Verificar si el empleado está disponible
    emp_disponible = False
    for emp in empleados:
        if emp["nombre"] == empleado:
            if "disponible" in emp and emp["disponible"]:
                emp_disponible = True
                emp["disponible"] = False
                break
    if not emp_disponible:
        print("Error: el empleado no está disponible")
        return

    # Verificar si el cliente existe
    cliente_existente = False
    for cli in clientes:
        if cli["nombre"] == cliente:
            cliente_existente = True
            break
    if not cliente_existente:
        print("Error: el cliente no existe")
        return

    # Añadir el trabajo a la lista
    trabajos.append({
        "fecha": fecha,
        "cliente": cliente,
        "servicio": servicio,
        "empleado": empleado
    })
    print("Servicio registrado correctamente")
