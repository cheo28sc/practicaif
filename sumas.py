nombre = input("¿Cómo te llamas? ")  # Pide al usuario que introduzca su nombre
print("¡Hola " + nombre + "!")


x = ((4 + 8) / 2) / (3 * 7)
print(x)



# Pedimos al usuario el número de cajas y el precio por unidad
cajas = int(input("Ingrese el número de cajas compradas: "))
precio = float(input("Ingrese el precio por unidad: "))

# Calculamos el total a pagar
total = cajas * precio

# Mostramos el resultado por pantalla
print("El total a pagar es: $", total)



# Pedimos al usuario que ingrese un entero positivo
n = int(input("Ingrese un entero positivo: "))

# Calculamos la suma de cuadrados de los primeros n enteros positivos
suma = (n * (n + 1) * (2 * n + 1)) / 6

# Mostramos el resultado por pantalla
print("La suma de cuadrados de los primeros", n, "enteros positivos es:", suma)




# Pedimos al usuario el número de payasos y muñecas vendidos
payasos = int(input("Ingrese el número de payasos vendidos: "))
munecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calculamos el peso total del paquete y el promedio de peso de los juguetes
peso_payasos = payasos * 120
peso_munecas = munecas * 80
peso_total = peso_payasos + peso_munecas
promedio_peso = peso_total / (payasos + munecas)

# Mostramos los resultados por pantalla
print("El peso total del paquete es:", peso_total, "gramos")
print("El promedio de peso de los juguetes es:", promedio_peso, "gramos")
