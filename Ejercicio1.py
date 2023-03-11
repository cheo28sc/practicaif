# Pedir al usuario que ingrese una lista de 5 materias
print("--------------------------------------------")
materias = []
for i in range(5):
    
    materia = input("Ingrese una materia: ")
    materias.append(materia)

# Mostrar un mensaje "Yo estudio" para cada materia ingresada
print("--------------------------------------------")
for materia in materias:
    
    print("Yo estudio:", materia)

# Pedir al usuario que ingrese las notas de cada materia
print("--------------------------------------------")
notas = {}
for materia in materias:
    
    nota = input("¿Cuál es tu nota en " + materia + "? ")
    notas[materia] = nota

# Mostrar las notas de cada materia
print("--------------------------------------------")
print("\nTus notas son:")
for materia, nota in notas.items():
    print("- En " + materia + " has sacado " + nota)
    
    # Identificar las materias que se necesitan repetir
repetir = []
for materia, nota in notas.items():
    if float(nota) < 70:
        repetir.append(materia)
for materia in repetir:
    materias.remove(materia)

# Mostrar las materias que se han aprobado y las que se necesitan repetir

if repetir:
    print("---------------------------------------------")
    print("\nTendrás que repetir las siguientes materias:")
    for materia in repetir:
        print("- " + materia)
else:
    print("--------------------------------------------")
    print("\n¡Excelente, no tienes que repetir ninguna materia!")