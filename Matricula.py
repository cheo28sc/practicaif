def ingresar_datos_usuario():
    nombre = input("Ingrese su nombre completo: ")
    cedula = input("Ingrese su número de cédula: ")
    edad = input("Ingrese su edad: ")
    return nombre, cedula, edad

def matricular_cursos():
    cursos = []
    while True:
        curso = input("Ingrese el nombre del curso (o presione Enter para salir): ")
        if curso == "":
            break
        cursos.append(curso)
    return cursos

def calcular_promedio(curso):
    examen1 = float(input(f"Ingrese la nota del Examen 1 de {curso}: "))
    examen2 = float(input(f"Ingrese la nota del Examen 2 de {curso}: "))
    examen3 = float(input(f"Ingrese la nota del Examen 3 de {curso}: "))
    promedio = (examen1 + examen2 + examen3) / 3
    return promedio

def calcular_total_pagar(cursos):
    total = len(cursos) * 35000
    descuento = 0
    if total > 140000:
        descuento = 0.15
    elif total > 104000:
        descuento = 0.1
    elif total > 69000:
        descuento = 0.05
    total_con_descuento = total * (1 - descuento)
    return total, total_con_descuento, descuento

def facturar_cursos(total, total_con_descuento, descuento):
    print(f"Total sin descuento: {total}")
    print(f"Descuento: {descuento*100}%")
    print(f"Total con descuento: {total_con_descuento}")

while True:
    print("1. Ingresar datos de usuario.")
    print("2. Matricular cursos.")
    print("3. Calcular promedios.")
    print("4. Facturar cursos.")
    print("5. Salir.")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        nombre, cedula, edad = ingresar_datos_usuario()
        print(f"Nombre: {nombre}")
        print(f"Cédula: {cedula}")
        print(f"Edad: {edad}")
    elif opcion == 2:
        cursos = matricular_cursos()
        print(f"Cursos matriculados: {cursos}")
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
