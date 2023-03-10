##Ejemplo for, imprime los 20 primeros numeros en una linea

# for i in range(20):
#     print(i, end=" ") #imprimir numero, sin salto linea
# print() #lin

# varios = ['Rojo', 7 , 10]
# suma = varios[1] + varios[2]

# print(f"Mi color favorito es el {varios[0]} y como resultado: {suma}.")
    
    
#
from  tkinter import *
import time

#FUNCION PARA ACTUALIZAR LA HORA
def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time,bg="black",fg="green",font="Arial 50 bold")
	clock.after(200,times)
	
#VENTANA
root=Tk()
root.geometry("485x250")
root.title("Reloj digital con Tkinter")
clock=Label(root,font=("times",50,"bold"))

clock.grid(row=2,column=1,pady=25,padx=100)
times()

digi=Label(root,text=" Hora Actual",font="times 24 bold",fg="red")
digi.grid(row=0,column=1)

root.mainloop()

#agregar un numero a una lista
# a = [1,2,3,4,5]
# a.append (6)
# print (a)
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# for subject in subjects:
#     print("Yo estudio " + subject)
    
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.   
#     subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# print(subjects)
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# scores = []
# for subject in subjects:
#     score = input("¿Qué nota has sacado en " + subject + "?")
#     scores.append(score)
# for i in range(len(subjects)):
#     print("En " + subjects[i] + " has sacado " + scores[i])
    
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.    
awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))



#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")
    
    #solucion 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")




#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
subjects = ["Matemáticas", "Física", "Química", "Historia", "Español"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 70:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))  

#solucion 2
subjects = ["Matemáticas", "Física", "Química", "Historia", "Español"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 70:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))




#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for i in range(len(alphabet), 1, -1):
#     if i % 3 == 0:
#         alphabet.pop(i-1)
# print(alphabet)

#solucion 2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for i in range(len(alphabet), 1, -1):
#     if i % 3 == 0:
#         alphabet.pop(i-1)
# print(alphabet)



#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    
    


#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.   
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
    
    


#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.    
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))  




#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 



