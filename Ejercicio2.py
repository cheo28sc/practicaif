# Pedir al usuario los números ganadores del Lotto
print("**********************************")
numeros_ganadores = []
for i in range(5):
    
    numero = int(input("Ingrese el número ganador: "))
    numeros_ganadores.append(numero)

numeros_ganadores.sort()
print("**********************************")
print("Los números ganadores son:", end=" ")
for numero in numeros_ganadores:
    print(numero, end=", ")




