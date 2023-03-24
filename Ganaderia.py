import os

class Ganado:
    def __init__(self, codigo, nombre, peso, fecha_ingreso, nombre_madre, nombre_padre):
        self.codigo = codigo
        self.nombre = nombre
        self.peso = peso
        self.fecha_ingreso = fecha_ingreso
        self.nombre_madre = nombre_madre
        self.nombre_padre = nombre_padre

    def __str__(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Peso: {self.peso}, Fecha de ingreso: {self.fecha_ingreso}, Nombre madre: {self.nombre_madre}, Nombre padre: {self.nombre_padre}"

class Ganaderia:
    def __init__(self):
        self.ganado = []
        self.archivo = 'ganado.txt'
        if os.path.isfile(self.archivo):
            with open(self.archivo, 'r') as f:
                for linea in f:
                    codigo, nombre, peso, fecha_ingreso, nombre_madre, nombre_padre = linea.strip().split(';')
                    self.ganado.append(Ganado(codigo, nombre, peso, fecha_ingreso, nombre_madre, nombre_padre))

    def ingresar_ganado(self):
        codigo = input("Ingrese el codigo de ganado: ")
        nombre = input("Ingrese el nombre de ganado: ")
        peso = input("Ingrese el peso de ganado: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso de ganado (DD/MM/AAAA): ")
        nombre_madre = input("Ingrese el nombre de la madre de ganado: ")
        nombre_padre = input("Ingrese el nombre del padre de ganado: ")
        self.ganado.append(Ganado(codigo, nombre, peso, fecha_ingreso, nombre_madre, nombre_padre))
        self.guardar_ganado()
        print("Ganado ingresado exitosamente.")

    def consultar_ganado(self):
        codigo = input("Ingrese el codigo de ganado: ")
        for animal in self.ganado:
            if animal.codigo == codigo:
                print(animal)
                return
        print(f"No se encontro el ganado con codigo {codigo}.")

    def modificar_ganado(self):
        codigo = input("Ingrese el codigo de ganado: ")
        for animal in self.ganado:
            if animal.codigo == codigo:
                animal.nombre = input("Ingrese el nuevo nombre de ganado: ")
                animal.peso = input("Ingrese el nuevo peso de ganado: ")
                animal.fecha_ingreso = input("Ingrese la nueva fecha de ingreso de ganado (DD/MM/AAAA): ")
                animal.nombre_madre = input("Ingrese el nuevo nombre de la madre de ganado: ")
                animal.nombre_padre = input("Ingrese el nuevo nombre del padre de ganado: ")
                self.guardar_ganado()
                print("Ganado modificado exitosamente.")
                return
        print(f"No se encontro el ganado con codigo {codigo}.")

    def eliminar_ganado(self):
        codigo = input("Ingrese el codigo de ganado: ")
        for animal in self.ganado:
            if animal.codigo == codigo:
                self.ganado.remove(animal)
                self.guardar_ganado()
                print("Ganado eliminado exitosamente.")
                return
        print(f"No se encontro el ganado con codigo {codigo}.")

    
