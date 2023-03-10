#Problema 1 definir una lista imprima en pantalla

lista = []

for x in range (5):
    valor =  int (input("ingrese un valor entero: "))
    lista.append(valor)
    #imprimir
print (lista)


#problema 2
lista2 = []
valor2 =  int (input("ingrese un valor entero: "))
while valor != 0:
    lista2.append(valor2)
    valor2 =  int (input("ingrese un valor entero: "))
print ("tamaño de la lista ", len(lista2))